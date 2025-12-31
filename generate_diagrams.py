# generate_diagrams.py
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from matplotlib.path import Path
from matplotlib.patches import FancyBboxPatch

def create_container_arch():
    """Generate container architecture diagram for Ollama"""
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    # Background color
    ax.add_patch(patches.Rectangle((0, 0), 10, 8, facecolor='#f0f8ff', edgecolor='none'))
    
    # Title
    plt.text(5, 7.5, 'Ollama Containerized Model Management Architecture', 
             fontsize=16, ha='center', fontweight='bold')
    
    # Model layer
    ax.add_patch(patches.Rectangle((2, 5), 6, 1.5, facecolor='#e6f7ff', 
                                 edgecolor='#1890ff', linewidth=1.5))
    plt.text(5, 5.75, 'Model Layer', fontsize=14, ha='center', fontweight='bold')
    plt.text(5, 5.2, 'GGUF Format Model File\n(mistral:7b-instruct-q4_0)', 
             fontsize=12, ha='center')
    
    # Runtime layer
    ax.add_patch(patches.Rectangle((2, 3), 6, 1.5, facecolor='#f6ffed', 
                                 edgecolor='#52c41a', linewidth=1.5))
    plt.text(5, 3.75, 'Runtime Layer', fontsize=14, ha='center', fontweight='bold')
    plt.text(5, 3.2, 'Inference Engine (llama.cpp)\nAutomatic Backend Selection (CUDA/Metal/Vulkan)', 
             fontsize=12, ha='center')
    
    # API layer
    ax.add_patch(patches.Rectangle((2, 1), 6, 1.5, facecolor='#fff7e6', 
                                 edgecolor='#fa8c16', linewidth=1.5))
    plt.text(5, 1.75, 'API Layer', fontsize=14, ha='center', fontweight='bold')
    plt.text(5, 1.2, 'RESTful API\nOpenAI Format Compatible', fontsize=12, ha='center')
    
    # Arrows
    codes = [Path.MOVETO, Path.LINETO]
    arrow_props = dict(arrowstyle='->', lw=2, color='gray')
    
    # Model layer -> Runtime layer
    path = Path([(5, 5), (5, 4.5)], codes)
    patch = patches.PathPatch(path, facecolor='none', edgecolor='gray', lw=1.5)
    ax.add_patch(patch)
    ax.annotate('', xy=(5, 4.5), xytext=(5, 5), arrowprops=arrow_props)
    
    # Runtime layer -> API layer
    path = Path([(5, 3), (5, 2.5)], codes)
    patch = patches.PathPatch(path, facecolor='none', edgecolor='gray', lw=1.5)
    ax.add_patch(patch)
    ax.annotate('', xy=(5, 2.5), xytext=(5, 3), arrowprops=arrow_props)
    
    # Client connections
    ax.plot([1, 2], [2, 2], 'k-', linewidth=1.5)
    ax.plot([8, 9], [2, 2], 'k-', linewidth=1.5)
    plt.text(0.5, 2, 'Client Applications', fontsize=12, ha='right')
    plt.text(9.5, 2, 'Client Applications', fontsize=12, ha='left')
    
    # Device label
    plt.text(5, 0.3, 'Edge Device (Laptop/Server)', fontsize=12, ha='center', 
             bbox=dict(facecolor='white', edgecolor='gray', alpha=0.7))
    
    plt.tight_layout()
    plt.savefig('container_arch.png', dpi=300, bbox_inches='tight')
    print("✅ Generated container_arch.png")

def create_mode_comparison():
    """Generate deployment mode comparison chart"""
    modes = ['Cloud API', 'Local Ollama', 'Hybrid Mode']
    response_times = [3.8, 1.2, 2.1]  # seconds
    privacy_scores = [2, 10, 8]  # privacy score (1-10)
    cost_scores = [10, 2, 5]  # cost score (1-10, lower is better)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Response time
    bars1 = ax.bar([0, 1, 2], response_times, width=0.6, color='#1890ff', 
                  label='Response Time (seconds)')
    ax.set_ylabel('Response Time (seconds)', color='#1890ff', fontsize=12)
    ax.tick_params(axis='y', labelcolor='#1890ff')
    
    # Privacy score
    ax2 = ax.twinx()
    bars2 = ax2.bar([0.3, 1.3, 2.3], privacy_scores, width=0.6, color='#52c41a', 
                   alpha=0.7, label='Privacy Score')
    ax2.set_ylabel('Privacy Score (1-10)', color='#52c41a', fontsize=12)
    ax2.tick_params(axis='y', labelcolor='#52c41a')
    ax2.set_ylim(0, 11)
    
    # Cost score
    ax3 = ax.twinx()
    ax3.spines["right"].set_position(("axes", 1.1))
    bars3 = ax3.bar([0.6, 1.6, 2.6], cost_scores, width=0.6, color='#fa8c16', 
                   alpha=0.7, label='Cost Score')
    ax3.set_ylabel('Cost Score (1-10, lower is better)', color='#fa8c16', fontsize=12)
    ax3.tick_params(axis='y', labelcolor='#fa8c16')
    ax3.set_ylim(0, 11)
    
    # Labels and title
    ax.set_title('Comparison of Three LLM Deployment Modes', fontsize=16, pad=20)
    ax.set_xticks([0.5, 1.5, 2.5])
    ax.set_xticklabels(modes, fontsize=12)
    ax.set_xlabel('Deployment Mode', fontsize=12)
    
    # Add data labels
    for i, v in enumerate(response_times):
        ax.text(i, v + 0.2, f'{v:.1f}s', ha='center', fontsize=10)
    
    for i, v in enumerate(privacy_scores):
        ax2.text(i+0.3, v + 0.3, f'{v}', ha='center', fontsize=10)
    
    for i, v in enumerate(cost_scores):
        ax3.text(i+0.6, v + 0.3, f'{v}', ha='center', fontsize=10)
    
    # Legend
    from matplotlib.lines import Line2D
    legend_elements = [
        Line2D([0], [0], color='#1890ff', lw=4, label='Response Time (seconds)'),
        Line2D([0], [0], color='#52c41a', lw=4, label='Privacy Score'),
        Line2D([0], [0], color='#fa8c16', lw=4, label='Cost Score')
    ]
    ax.legend(handles=legend_elements, loc='upper center', 
              bbox_to_anchor=(0.5, -0.15), ncol=3)
    
    plt.tight_layout()
    plt.savefig('mode_comparison.png', dpi=300, bbox_inches='tight')
    print("✅ Generated mode_comparison.png")

def create_hybrid_arch():
    """Generate hybrid cloud-edge AI architecture diagram"""
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Title
    plt.text(6, 9.5, 'Hybrid AI Architecture for Cloud-Edge Collaboration', 
             fontsize=18, ha='center', fontweight='bold')
    
    # Cloud area
    ax.add_patch(patches.Rectangle((0.5, 5.5), 11, 3.5, facecolor='#f0f2f5', 
                                 edgecolor='#1890ff', linewidth=1.5, linestyle='--'))
    plt.text(6, 8.7, 'Central Cloud', fontsize=14, ha='center', fontweight='bold')
    
    # Cloud components
    ax.add_patch(patches.Ellipse((3, 7.5), 1.5, 0.8, facecolor='#e6f7ff', edgecolor='#1890ff'))
    plt.text(2.2, 7.5, 'Model Training Cluster', fontsize=10)
    
    ax.add_patch(patches.Ellipse((6, 7.5), 1.5, 0.8, facecolor='#e6f7ff', edgecolor='#1890ff'))
    plt.text(5, 7.5, 'Knowledge Distillation Service', fontsize=10)
    
    ax.add_patch(patches.Ellipse((9, 7.5), 1.5, 0.8, facecolor='#e6f7ff', edgecolor='#1890ff'))
    plt.text(8.5, 7.5, 'Model Repository', fontsize=10)
    
    # Edge area
    ax.add_patch(patches.Rectangle((0.5, 1), 11, 3.5, facecolor='#f6ffed', 
                                 edgecolor='#52c41a', linewidth=1.5, linestyle='--'))
    plt.text(6, 4.2, 'Edge Layer', fontsize=14, ha='center', fontweight='bold')
    
    # Edge nodes - WITH ROUNDED CORNERS
    for i, x in enumerate([2, 6, 10]):
        # Create a rounded rectangle using FancyBboxPatch
        rect = FancyBboxPatch((x-1, 2), 2, 1.5, 
                             boxstyle="round,pad=0.1",
                             facecolor='white',
                             edgecolor='#fa8c16',
                             linewidth=1.5)
        ax.add_patch(rect)
        
        plt.text(x, 2.75, f'Edge Node {i+1}', fontsize=10, ha='center')
        plt.text(x, 2.3, 'Ollama Service', fontsize=9, ha='center')
        plt.text(x, 1.8, 'Mistral-7B-Q4_0', fontsize=9, ha='center')
    
    # Cloud-edge connections
    for x in [2, 6, 10]:
        ax.plot([x, x], [3.5, 5.5], 'k--', linewidth=1, alpha=0.7)
        plt.text(x, 4.5, 'Secure Channel', fontsize=8, ha='center', rotation=90)
    
    # Cloud internal connections
    ax.plot([4, 5], [7.5, 7.5], 'k-', linewidth=1.5)
    ax.plot([7, 8], [7.5, 7.5], 'k-', linewidth=1.5)
    
    # Cloud-edge collaboration components
    ax.add_patch(patches.Rectangle((4, 4.5), 4, 0.8, facecolor='#fff7e6', 
                                 edgecolor='#fa8c16', linewidth=1))
    plt.text(6, 4.9, 'Collaboration Mechanisms', fontsize=10, ha='center', fontweight='bold')
    plt.text(6, 4.5, 'Intelligent Routing | Model Federation | Unified Management', 
             fontsize=9, ha='center')
    
    plt.tight_layout()
    plt.savefig('hybrid_arch.png', dpi=300, bbox_inches='tight')
    print("✅ Generated hybrid_arch.png")

if __name__ == "__main__":
    create_container_arch()
    create_mode_comparison()
    create_hybrid_arch()
    print("\nAll diagrams generated successfully!")
