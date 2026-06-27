import os
import subprocess

# Define the fold paths and model_mm_types
fold_paths = [
    "PS3_Splits/tcga-coadread/TCGA_COADREAD_overall_survival_k=0",
    "PS3_Splits/tcga-coadread/TCGA_COADREAD_overall_survival_k=1",
    "PS3_Splits/tcga-coadread/TCGA_COADREAD_overall_survival_k=2",
    "PS3_Splits/tcga-coadread/TCGA_COADREAD_overall_survival_k=3",
    "PS3_Splits/tcga-coadread/TCGA_COADREAD_overall_survival_k=4",
]

model_mm_types = ["histo", "gene", 'text']

# Path to the main script
main_script = "main_survival.py"

# Base command
base_command = [
    "python",
    main_script,
]

# Iterate through folds and model_mm_types
for fold_path in fold_paths:
    for model_mm_type in model_mm_types:
        # Define arguments
        if model_mm_type == 'text':
            args = [
                f"--split_dir={fold_path}",
                f"--model_mm_type={model_mm_type}",
                "--process_text=True",
            ]
        else:
            args = [
                f"--split_dir={fold_path}",
                f"--model_mm_type={model_mm_type}",
                "--process_text=False",
            ]

        # Combine base command and arguments
        command = base_command + args

        print(f"Running command: {' '.join(command)}")

        # Run the command
        subprocess.run(command)
