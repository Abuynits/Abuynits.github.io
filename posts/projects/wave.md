---
title: "Wave"
summary: "A Gesture-Controlled Human-Computer Interface (HCI)"
coverImage: "/assets/projects/wave/wave_overview.png"
order: 4 
---
**Example of WAVE detecting a swipe right gesture to switch desktops**


[Devpost link](https://devpost.com/software/wave-9cr4ni)

## Background

For Boilermake XI, my friends and I decided to create a different way of interacting with computers: through gestures. Our inspiration came from the info touch screen kiosk in LSWN which requires ~20N of force to register a 'touch'. 

So we created Wave. A gesture HCI which allows users to interact with their displays through personalized gestures.

## How does it work:

### Another Example:

<img src="/assets/projects/wave/wave_ex_2.png" width="600" height="600">

### Pose Detection

We choose to build on top of Google’s MediaPipe with a lightweight continual learnign model through a MLP. This enabled us to have continual learning and the flexibility to generate data, modify the model architecture, train + evaluate the model, and prepare the weights for new inference in < 5 sec. With this approach we can run inference at **30fps**, and expand the model architecture to **32 custom hand poses**.

### Gesture detection:

For a new user, the model starts out with no data, and when the user wants to append a new pose, Wave will record ~25 examples of 42 datapoints (x,y coordinates for the hand), normalize them + scale them to perform inference on any depth distance, quickly retrain the model, update the inference weights and then start evaluating again with the new model.

The model consists of 2 blocks of Linear, Relu, and dropout. The first block upscales the 42 x,y coordinates to a dimension of 64, then the next block’s output dimension is 32, and the last final linear layer is variable dependent on the number of output classes specified by the user. We finish with a softmax function and ignore outputs from models with 0 and 1 output classes. Additionally, we mark poses as n/a if they do not pass a 99% threshold in the softmax that is scaled down with the number of datapoints in the dataset.

Additionally we use analytical approaches through a weighted loss, applying more weights to the top of the fingers then to the palm in the rare cases the model fails and when the user starts using the model.

With only ~1k parameters, we can train for ~200 epoch with early stopping in 5 seconds on a M1 Mac.

### Motion tracking:

Once we have the poses of the hand (ie thumbs up, pointing left / right), we need to extract the motion of the hand.

Our pipeline is able to detect motion in the z-axis, rotations (cw / ccw), translation (left, right, down, up), and idle (stationary).

To accomplish this, we track the last 6-10 points and extract the index finger. We then track the (x,y,z) points of the index finger and the side radios + area of the bounding box that encloses these points.

If the bounding box is a rectangle (using the side ratios), we have translational motion (horizontal = x, vertical = y). If we have a square (using side ratios), we have a square and therefore either rotational or an idle pose.

We now look at the ratio of the square with respect to the whole scene captured by the camera. If the points are clustered, this implies that the hand is stationary, else if the points are not clustered, and in a square shape, this means that we have rotation. To detect rotation, we use the shoelace algorithm ( more [here](https://www.101computing.net/the-shoelace-algorithm/) ).

### Motion smoothing:

At 30 fps frame detection, the output poses have high granularity. For example, when a user moves to the left, and stops, they might jerk to the right, cause the sytem to detect a [left translation, idle, right translation, idle sequence] instead of simply a [left translation, idle sequence].

To account for this, we smooth the output data through d-bouncing. D-bounce limits the number of times a function can query from a source. Going back to our example, because the jerky motion from left → right translation happens in a short amount of time, d-bouncing will fetch the left translation, have a delay, miss fetching the right translation, and then when the delay is over, the function will then fetch the new updated state which be idle, effectively reducing jitteriness and allowing for smoother motion.

### Gesture Sequence Mapping:

Now comes the question of matching a raw data stream to a action that a user wants. First lest define a gesture as an ordered collection of pose, direction pairs. As an example, consider panning from the left side of the screen to the right side. We start in a stationary pose (lets say pointing up), then start moving in the right direction and end in another stationary pose, at the right side of the screen (lets say pointing down).

This creates a sequence defined as: point up → right motion → point down. And this is how a user defines gesture.

Now because there might be errors (lets say the user pauses and the sequence becomes point up → right motion → idle → right_motion → point down), we still want to match to this sequence. If the sequence matches the stream, we spawn a Matcher which looks for matches in the stream. If the Matcher doesnt match the whole sequence within a certain error window, it will destroy. When a Matcher matches, we remove all match objects because the User has inputted a gesture.

### Vision-Langauge Models:

To account for the cases when a gesture might be to complicated, we use a video language model, Video-LLaVA. Now instead of matching poses, we instead use a vector database created on the Bert Encoder that encodes descriptions of gestures and matches them based on cosine similarity.

Users will now describe a complicated motion that will be stored in a database. Then when the motion is performed and detected by our gesture sequencer mapper (start and end poses are both idle), we save those frames, send them to Llava along with a few multi-shot examples to tune the models responses and receive a description of the hand in 3-5 seconds. Finally we perform a cosine similarity match with this hand against the database of existing poses, performing the associated action.

### Frontend:

For the frontend, we chose to create a desktop app so that we could execute child processes for important tasks such as running a local flask server and writing to local files. Since we’re most familiar with web development, we ended up porting a Next.js web app through Electron.js, allowing us access to the local system with all the familiarity and benefits of a web app. In terms of the design, the entire UI, animations and transitions included, was developed only with TailwindCSS, JSX, and JavaScript (no external component libraries included).

We also built a fully functioning profile/account system into the application. When a user signs into our platform, we interface a MongoDB cluster stored on the cloud through Mongoose (a Node.js module) to verify user information, utilizing the bcrypt libary to store and compare encrypted passwords for maximum security. We also leveraged jsonwebtoken to insert cookies into the user’s system so they can stay logged in even after closing the app.

### Flask server:

For the Flask server, we wanted to make sure that we could interface our gesture recognition model with the frontend seamlessly. Our flask server runs multiple threads at once for camera video processing, model inference, and voice commands, without blocking the main server process.

### Open-interpreter:

We used a technology called open-interpreter to allow us to take a natural language input like “set my system to dark mode” and output the apple script necessary to make that happen.

### Voice interaction:

For this part of the project, we wanted to allow users to initiate a voice command through a waving gesture and through stating “Alright Wave” (which would serve as the wake function). We used PyAudio to record audio, whisper.cpp to transcribe audio, and open-interpreter to use that natural language for some computer function. Some voice commands include initiating gesture training, starting Wave (recording), and stopping Wave. The idea here was to give users a more convenient “hands-free” way to interact with our app. Additionally, we prototyped a way to interact with open-interpreter, which utilizes LLMs like GPT-4 to allow you to interact with your computer by generating and running code through your terminal. Unfortunately, this “enhanced Siri” idea did not make it into the finished product, as we felt implementing gesture commands was more important.

devpost + more documentation can be found [here](https://devpost.com/software/wave-9cr4ni).