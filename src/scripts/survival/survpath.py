import os
import subprocess

# Define the fold paths and model_mm_types
fold_paths = [
    "PS3_Splits/tcga-kirc/TCGA_KIRC_overall_survival_k=0",
    "PS3_Splits/tcga-kirc/TCGA_KIRC_overall_survival_k=1",
    "PS3_Splits/tcga-kirc/TCGA_KIRC_overall_survival_k=2",
    "PS3_Splits/tcga-kirc/TCGA_KIRC_overall_survival_k=3",
    "PS3_Splits/tcga-kirc/TCGA_KIRC_overall_survival_k=4",
]

bag_size=4096
batch_size=1
out_size=16
out_type='allcat'
model_tuple='MIL,default'
max_epoch=50
lr=0.0001
wd=0.00001
lr_scheduler='cosine'
opt='adamW'
grad_accum=1
loss_fn='nll'
n_label_bin=4
alpha=0.5
em_step=1
load_proto=1
es_flag=0
tau=1.0
eps=1
n_fc_layer=0
# Multimodal args
model_mm_type='survpath'
append_embed='random'
histo_agg='mean'
num_coattn_layers=1
model_config = 'MIL_default'
model = 'MIL'
# Path to the main script
main_script = "main_survival.py"

# Base command
base_command = [
    "python",
    main_script,
]

# Iterate through folds and model_mm_types

for fold_path in fold_paths:
    # Define arguments
    args = [
        f"--split_dir={fold_path}",
        f"--bag_size={bag_size}",
        f"--batch_size={batch_size}",
        f"--out_type={out_type}",
        f"--model_histo_type={model}",
        f"--model_histo_config={model_config}",
        f"--max_epochs={max_epoch}",
        f"--lr={lr}",
        f"--wd={wd}",
        f"--opt={opt}",
        f"--accum_steps={grad_accum}",
        f"--loss_fn={loss_fn}",
        f"--n_label_bins={n_label_bin}",
        f"--nll_alpha={alpha}",
        f"--em_iter={em_step}",
        f"--early_stopping={es_flag}",
        f"--tau={tau}",
        f"--ot_eps={eps}",
        f"--n_fc_layers={n_fc_layer}",
        f"--model_mm_type={model_mm_type}",
        f"--append_embed={append_embed}",
        f"--histo_agg={histo_agg}",
        f"--num_coattn_layers={num_coattn_layers}",
    ]

    # Combine base command and arguments
    command = base_command + args

    print(f"Running command: {' '.join(command)}")

    # Run the command
    subprocess.run(command)
