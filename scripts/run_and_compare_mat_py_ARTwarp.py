import subprocess
import os

def run_ARTwarp_MATLAB(input_folder, warpFactorLevel, vigilance, maxCats, maxIts, sampleInterval, randomiseSortOrder, output_folder):
    cmd = f"ARTwarp_cli_mode('{input_folder}', {warpFactorLevel}, {vigilance}, {maxCats}, {maxIts}, 'sampleInterval', {sampleInterval}, 'randomiseSortOrder', {randomiseSortOrder}, 'outputFolder', '{output_folder}')"
    os.chdir("C:/00-git-repos/artwarp")
    subprocess.run(["matlab", "-batch", cmd], capture_output=True, text=True)
    print(["matlab", "-batch", cmd])

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
    os.chdir("C:/00-git-repos/artwarp-py")
    subprocess.run(cmd)


def run_both_and_compare(input_folder,warpFactorLevel, vigilance, maxCats, maxIts, sampleInterval, randomiseSortOrder, output_folder):
    run_ARTwarp_MATLAB(input_folder, warpFactorLevel, vigilance, maxCats, maxIts, sampleInterval, randomiseSortOrder, output_folder)
    #run_ARTwarp_py(input_folder, warpFactorLevel, vigilance, maxCats, maxIts, sampleInterval, output_folder)
    #cmd = ["python",
            #"scripts/compare_categorizations.py",
            #f"{output_folder}/MATLAB_category_assignments.csv",
            #f"{output_folder}/category_assignments.csv"]
    #subprocess.run(cmd)

run_both_and_compare("C:/00-git-repos/artwarp/sarasota-50-5SWT-ctr", 3, 96, 50, 10000, 0.01, "false", "C:/00-git-repos/ARTwarp_both_test_run")
