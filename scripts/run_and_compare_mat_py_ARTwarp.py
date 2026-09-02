import subprocess

def run_ARTwarp_MATLAB(input_folder, warpFactorLevel, vigilance, maxCats, maxIts, sampleInterval, randomiseSortOrder, output_folder):
    cmd = f"ARTwarp_cli_mode('{input_folder}', {warpFactorLevel}, {vigilance}, {maxCats}, {maxIts}, 'sampleInterval', {sampleInterval}, 'randomiseSortOrder', {randomiseSortOrder}, 'outputFolder', {output_folder})"
    subprocess.run(["matlab", "-batch", cmd])

def run_ARTwarp_py(input_folder, warpFactorLevel, vigilance, maxCats, maxIts, sampleInterval, output_folder):
    cmd = [
        "python",
        "artwarp-py",
        "train",
        "-i", input_folder,
        "-o", f"{output_folder}/RESULTS.pkl",
        "--format", "ctr",
        "--vigilance", str(vigilance),
        "--learning-rate", "0.1",
        "--bias", "0.000001",
        "--max-categories", str(maxCats),
        "--max-iterations", str(maxIts),
        "--warp-factor", str(warpFactorLevel),
        "--sample-interval", str(sampleInterval),
        "--tempres", "0.005",
        "--export-categories"
    ]
    subprocess.run(cmd)


def run_both_and_compare(input_folder,warpFactorLevel, vigilance, maxCats, maxIts, sampleInterval, randomiseSortOrder, output_folder):
    run_ARTwarp_MATLAB(input_folder, warpFactorLevel, vigilance, maxCats, maxIts, sampleInterval, randomiseSortOrder, output_folder)
    run_ARTwarp_py(input_folder, warpFactorLevel, vigilance, maxCats, maxIts, sampleInterval, output_folder)
    cmd = ["python",
            "scripts/compare_categorizations.py",
            f"{output_folder}/MATLAB_category_assignments.csv",
            f"{output_folder}/category_assignments.csv"]
    subprocess.run(cmd)
