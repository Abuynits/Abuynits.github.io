import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def generate_compute_timeline_graph(data):
    """
    Generates a line graph of the GPU Compute Used Timeline 
    using Matplotlib and Pandas, with a table below instead of a legend.
    """
    # 1. Create a Pandas DataFrame from the input data
    df = pd.DataFrame(data)

    # 2. Setup the Matplotlib figure with two subplots (graph and table)
    fig = plt.figure(figsize=(14, 14))
    
    # Create grid: top for graph, bottom for table
    gs = fig.add_gridspec(2, 1, height_ratios=[2, 1], hspace=0.5)
    ax_graph = fig.add_subplot(gs[0])
    ax_table = fig.add_subplot(gs[1])

    # 3. Plot both TFLOPS lines
    ax_graph.plot(range(len(df)), df['Max TFLOPS Used (Mixed)'], 
            linewidth=3, color='#FF6B6B', alpha=0.6, label='Max TFLOPS Used (Mixed)', linestyle='--')
    
    ax_graph.plot(range(len(df)), df['Max Cumulative TFLOPS Used (Mixed)'], 
            linewidth=3, color='#4ECDC4', alpha=0.8, label='Max Cumulative TFLOPS Used (Mixed)')

    # 4. Add labels for 'Max TFLOPS Used (Mixed)' above each point
    for i, row in df.iterrows():
        label_value = row['Max TFLOPS Used (Mixed)']
        
        if label_value >= 1.0: 
            x = i
            y = label_value
            offset = 0.4
            ax_graph.text(x, y * offset, f'{label_value:,.1f}', 
                    fontsize=11, ha='center', va='bottom',
                    color='black', fontweight='bold', zorder=6)
        
        elif label_value > 0:
             ax_graph.text(i, row['Max Cumulative TFLOPS Used (Mixed)'] * 0.9, f'{label_value:,.1f}', 
                    fontsize=10, ha='center', va='top',
                    color='black', fontweight='bold', zorder=6)

    # 5. Mark all points with events
    colors = ['#FF6B6B', '#FFA07A', '#98D8C8', '#F7DC6F', '#BB8FCE', 
              '#85C1E2', '#F8B739', '#52B788', '#E76F51', '#2A9D8F',
              '#E63946', '#457B9D', '#06D6A0']
    
    for i, row in df.iterrows():
        if row['Status/Purpose']:
            ax_graph.scatter(i, row['Max Cumulative TFLOPS Used (Mixed)'], 
                       s=150, color=colors[i % len(colors)], 
                       edgecolors='black', linewidth=1.5, zorder=5)

    # 6. Customize the graph
    ax_graph.set_xlabel('Timeline', fontsize=12, fontweight='bold')
    ax_graph.set_ylabel('TFLOPS (Mixed Precision) (Log Scale)', fontsize=12, fontweight='bold')
    ax_graph.set_title('Happiness ∝ log(TFLOPS)', fontsize=18, fontweight='bold', pad=20)
    
    ax_graph.set_yscale('log')
    ax_graph.set_xticks(range(len(df)))
    ax_graph.set_xticklabels(df['Year Acquired'], rotation=45, ha='right', fontsize=10)
    ax_graph.grid(True, which="major", alpha=0.3, linestyle='--', linewidth=0.7)
    ax_graph.set_axisbelow(True)
    ax_graph.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x:,.0f}'))
    
    # Add simple legend for the lines
    ax_graph.legend(loc='upper left', fontsize=10)

    # 7. Create table below the graph
    ax_table.axis('off')
    
    # Prepare table data - only rows with events
    table_data = []
    for i, row in df.iterrows():
        if row['Status/Purpose']:
            # Create a colored square marker for the color column
            color_marker = '●'
            table_data.append([
                row['Year Acquired'],
                row['Status/Purpose'],
                row['Used Configuration']
            ])
    
    # Create the table
    table = ax_table.table(
        cellText=table_data,
        colLabels=['Date', 'Event/Status', 'GPU Configuration'],
        cellLoc='left',
        loc='center',
        colWidths=[0.12, 0.5, 0.38]
    )
    
    # Style the table
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1, 2)
    
    # Color the first column cells to match the markers
    event_idx = 0
    for i, row in df.iterrows():
        if row['Status/Purpose']:
            # Color the cell background in the Date column
            table[(event_idx + 1, 0)].set_facecolor(colors[i % len(colors)])
            table[(event_idx + 1, 0)].set_text_props(weight='bold', color='white')
            event_idx += 1
    
    # Style header row
    for j in range(3):
        table[(0, j)].set_facecolor('#40466E')
        table[(0, j)].set_text_props(weight='bold', color='white')

    plt.tight_layout()
    plt.show()

# --- DATA SECTION ---

COMPUTE_DATA = {
    'Year Acquired': ["May '22", "Jun '22", "Nov '22", "Dec '22", "Aug '23", "Oct '23", 
                      "Sept '24", "May '25", "Jul '25", "Aug '25", "Sept '25", "Oct '25", "Nov '25"],
    'Status/Purpose': ['', 'Started tinkering in ML using Torch / TF tutorials', 'Gifted by a mentor :)', 
                       'Colab Pro tier from TE Connectivity AI Cup', 'Joined CoRAL Lab', 'starting interning @ Armada AI', 
                       'Joined CoMMA Lab', 'left CoRAL, CoMMA, Armada AI. Started interning at Persona AI', 
                       'setup ssh connections to unused / idle PCs at Persona', 
                       'setup ssh connections to pcs in other office at persona', 'Left Persona. No Gpus. Big Sad.', 
                       'Joined Wang Lab @ UCSD', 'Access to NRP Compute Cluster. We made it in life.'],
    'Max TFLOPS Used (Mixed)': [0.3, 65.0, 1.3, 125.0, 284.0, 1248.0, 642.0, 330.0, 990.0, 1650.0, 27.2, 1786.8, 21120.0],
    'Max Cumulative TFLOPS Used (Mixed)': [0.3, 65.0, 65.0, 125.0, 284.0, 1248.0, 1248.0, 1248.0, 1248.0, 1650.0, 1650.0, 1786.8, 21120.0],
    'Used Configuration': ['1x 2020 mpb 13\'', '1 x Tesla T4', '1 x Jetson TX2', '1 x Tesla V100', '2 x RTX 3090', 
                           '4 x A100s', '1x A100, 1x 4090', '1x 4090', '3x 4090s', 
                           '2x 4090s + 2x 5090s', '1x Apple M2 Max', '4x 3090s, 4x A5000s, 1x 4090', '64 x 4090s']
}

# --- EXECUTION ---

if __name__ == '__main__':
    generate_compute_timeline_graph(COMPUTE_DATA)