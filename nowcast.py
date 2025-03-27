import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

def plot_statebased(data):
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(20, 7))

    # First plot
    data.plot.scatter(x='candidate_sb_best_sum_nokgi_ln1', y='sb_final_best_ln',
                                      marker='o', linewidth=3, s=2, alpha=.2, color='crimson', ax=axes[0])
    dots1 = axes[0].collections[-1]
    offsets1 = dots1.get_offsets()
    jittered_offsets1 = offsets1 + np.random.uniform(0, .3, offsets1.shape)
    dots1.set_offsets(jittered_offsets1)
    
    # ADD DASHED DIAGONAL LINE
    axes[0].plot([0, 10], [0, 10], linestyle='--', alpha = .4, color='gray')

    axes[0].set_xlim([0, 10])
    axes[0].set_ylim([0, 10])
    axes[0].set_title('UCDP Candidate vs UCDP GED Final (country-month)', weight="bold", size=14)
    axes[0].set_ylabel('UCDP GED Final Fatalities (ln+1)', fontsize=12)
    axes[0].set_xlabel('UCDP Candidate Fatalities (ln+1)', fontsize=12)

    # Second plot
    data.plot.scatter(x='candidate_sb_best_sum_nokgi_ln1', y='acled_sb_fat_ln',
                                      marker='o', linewidth=3, s=2, alpha=.2, color='crimson', ax=axes[1])
    dots2 = axes[1].collections[-1]
    offsets2 = dots2.get_offsets()
    jittered_offsets2 = offsets2 + np.random.uniform(0, .3, offsets2.shape)
    dots2.set_offsets(jittered_offsets2)

    # ADD DASHED DIAGONAL LINE
    axes[1].plot([0, 10], [0, 10], linestyle='--', alpha = .4, color='gray')
    
    axes[1].set_xlim([0, 10])
    axes[1].set_ylim([0, 10])
    axes[1].set_title('UCDP Candidate vs ACLED (country-month)', weight="bold", size=14)
    axes[1].set_ylabel('ACLED Fatalities (ln+1)', fontsize=12)
    axes[1].set_xlabel('UCDP Canidate Fatalities (ln+1)', fontsize=12)

    # Third plot
    data.plot.scatter(x='acled_sb_fat_ln', y='sb_final_best_ln',
                                      marker='o', linewidth=3, s=2, alpha=.2, color='crimson', ax=axes[2])
    dots3 = axes[2].collections[-1]
    offsets3 = dots3.get_offsets()
    jittered_offsets3 = offsets3 + np.random.uniform(0, .3, offsets3.shape)
    dots3.set_offsets(jittered_offsets3)

    # ADD DASHED DIAGONAL LINE
    axes[2].plot([0, 10], [0, 10], linestyle='--', alpha = .4, color='gray')
    
    axes[2].set_xlim([0, 10])
    axes[2].set_ylim([0, 10])
    axes[2].set_title('ACLED vs UCDP GED Final (country-month)', weight="bold", size=14)
    axes[2].set_ylabel('UCDP GED Final Fatalities (ln+1)', fontsize=12)
    axes[2].set_xlabel('ACLED Fatalities (ln+1)', fontsize=12)

    for axis in axes:
        for ax in [axis.xaxis, axis.yaxis]:
            ax.set_major_formatter(ScalarFormatter())
               
    fig.suptitle('Comparison of State-based Fatalities Data', fontsize=22, weight="bold", y=1.05)               
    plt.tight_layout()
    plt.show()


def plot_nonstate(data):
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(20, 7))

    # First plot
    data.plot.scatter(x='candidate_ns_best_sum_nokgi_ln1', y='ns_final_best_ln',
                                      marker='o', linewidth=3, s=2, alpha=.2, color='crimson', ax=axes[0])
    dots1 = axes[0].collections[-1]
    offsets1 = dots1.get_offsets()
    jittered_offsets1 = offsets1 + np.random.uniform(0, .3, offsets1.shape)
    dots1.set_offsets(jittered_offsets1)
    
    # ADD DASHED DIAGONAL LINE
    axes[0].plot([0, 10], [0, 10], linestyle='--', alpha = .4, color='gray')
    
    axes[0].set_xlim([0, 10])
    axes[0].set_ylim([0, 10])
    axes[0].set_title('UCDP Candidate vs UCDP GED Final (country-month)', weight="bold", size=14)
    axes[0].set_ylabel('UCDP GED Final Fatalities (ln+1)', fontsize=12)
    axes[0].set_xlabel('UCDP Candidate Fatalities (ln+1)', fontsize=12)

    # Second plot
    data.plot.scatter(x='candidate_ns_best_sum_nokgi_ln1', y='acled_ns_fat_ln',
                                      marker='o', linewidth=3, s=2, alpha=.2, color='crimson', ax=axes[1])
    dots2 = axes[1].collections[-1]
    offsets2 = dots2.get_offsets()
    jittered_offsets2 = offsets2 + np.random.uniform(0, .3, offsets2.shape)
    dots2.set_offsets(jittered_offsets2)

    # ADD DASHED DIAGONAL LINE
    axes[1].plot([0, 10], [0, 10], linestyle='--', alpha = .4, color='gray')
    
    axes[1].set_xlim([0, 10])
    axes[1].set_ylim([0, 10])
    axes[1].set_title('UCDP Candidate vs ACLED (country-month)', weight="bold", size=14)
    axes[1].set_ylabel('ACLED Fatalities (ln+1)', fontsize=12)
    axes[1].set_xlabel('UCDP Canidate Fatalities (ln+1)', fontsize=12)

    # Third plot
    data.plot.scatter(x='acled_ns_fat_ln', y='ns_final_best_ln',
                                      marker='o', linewidth=3, s=2, alpha=.2, color='crimson', ax=axes[2])
    dots3 = axes[2].collections[-1]
    offsets3 = dots3.get_offsets()
    jittered_offsets3 = offsets3 + np.random.uniform(0, .3, offsets3.shape)
    dots3.set_offsets(jittered_offsets3)

    # ADD DASHED DIAGONAL LINE
    axes[2].plot([0, 10], [0, 10], linestyle='--', alpha = .4, color='gray')
    
    axes[2].set_xlim([0, 10])
    axes[2].set_ylim([0, 10])
    axes[2].set_title('UCDP GED Final vs ACLED (country-month)', weight="bold", size=14)
    axes[2].set_xlabel('ACLED Fatalities (ln+1)', fontsize=12)
    axes[2].set_ylabel('UCDP GED Final Fatalities (ln+1)', fontsize=12)

    for axis in axes:
        for ax in [axis.xaxis, axis.yaxis]:
            ax.set_major_formatter(ScalarFormatter())
        
    fig.suptitle('Comparison of Non-state Fatalities Data', fontsize=22, weight="bold", y=1.05)        
    plt.tight_layout()
    plt.show()
    
    
def plot_onesided(data):  
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(20, 7))

    # First plot
    data.plot.scatter(x='candidate_os_best_sum_nokgi_ln1', y='os_final_best_ln',
                                      marker='o', linewidth=3, s=2, alpha=.2, color='crimson', ax=axes[0])
    dots1 = axes[0].collections[-1]
    offsets1 = dots1.get_offsets()
    jittered_offsets1 = offsets1 + np.random.uniform(0, .3, offsets1.shape)
    dots1.set_offsets(jittered_offsets1)
    
    # ADD DASHED DIAGONAL LINE
    axes[0].plot([0, 10], [0, 10], linestyle='--', alpha = .4, color='gray')
    
    axes[0].set_xlim([0, 10])
    axes[0].set_ylim([0, 10])
    axes[0].set_title('UCDP Candidate vs UCDP GED Final (country-month)', weight="bold", size=14)
    axes[0].set_ylabel('UCDP GED Final Fatalities (ln+1)', fontsize=12)
    axes[0].set_xlabel('UCDP Candidate Fatalities (ln+1)', fontsize=12)

    # Second plot
    data.plot.scatter(x='candidate_os_best_sum_nokgi_ln1', y='acled_os_fat_ln',
                                      marker='o', linewidth=3, s=2, alpha=.2, color='crimson', ax=axes[1])
    dots2 = axes[1].collections[-1]
    offsets2 = dots2.get_offsets()
    jittered_offsets2 = offsets2 + np.random.uniform(0, .3, offsets2.shape)
    dots2.set_offsets(jittered_offsets2)

    # ADD DASHED DIAGONAL LINE
    axes[1].plot([0, 10], [0, 10], linestyle='--', alpha = .4, color='gray')
    
    axes[1].set_xlim([0, 10])
    axes[1].set_ylim([0, 10])
    axes[1].set_title('UCDP Candidate vs ACLED (country-month)', weight="bold", size=14)
    axes[1].set_ylabel('ACLED Fatalities (ln+1)', fontsize=12)
    axes[1].set_xlabel('UCDP Canidate Fatalities (ln+1)', fontsize=12)

    # Third plot
    data.plot.scatter(x='acled_ns_fat_ln', y='os_final_best_ln',
                                      marker='o', linewidth=3, s=2, alpha=.2, color='crimson', ax=axes[2])
    dots3 = axes[2].collections[-1]
    offsets3 = dots3.get_offsets()
    jittered_offsets3 = offsets3 + np.random.uniform(0, .3, offsets3.shape)
    dots3.set_offsets(jittered_offsets3)

    # ADD DASHED DIAGONAL LINE
    axes[2].plot([0, 10], [0, 10], linestyle='--', alpha = .4, color='gray')
    
    axes[2].set_xlim([0, 10])
    axes[2].set_ylim([0, 10])
    axes[2].set_title('UCDP GED Final vs ACLED (country-month)', weight="bold", size=14)
    axes[2].set_xlabel('ACLED Fatalities (ln+1)', fontsize=12)
    axes[2].set_ylabel('UCDP GED Final Fatalities (ln+1)', fontsize=12)

    for axis in axes:
        for ax in [axis.xaxis, axis.yaxis]:
            ax.set_major_formatter(ScalarFormatter())
        
    fig.suptitle('Comparison of One-sided Fatalities Data', fontsize=22, weight="bold", y=1.05)                
    plt.tight_layout()
    plt.show()
    
    
    