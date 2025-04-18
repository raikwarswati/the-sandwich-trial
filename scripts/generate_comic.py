import requests
import json
import random
import os
import csv
from pathlib import Path
from datetime import datetime

script_file_name = 'Hotdog_Manga_Prompts_Full_Descriptive'

# Constants
COMFY_API = "http://127.0.0.1:8188"
CSV_PATH = Path(f"/teamspace/studios/this_studio/inputs/{script_file_name}.csv")
WORKFLOW_PATH = Path("/teamspace/studios/this_studio/ComfyUI/workflows/manga_workflows_2.json")
OUTPUT_FOLDER = f"{script_file_name}"
OUTPUT_DIR = Path(f"/teamspace/studios/this_studio/outputs/{OUTPUT_FOLDER}")
LOG_FILE = OUTPUT_DIR / "generation_log.csv"
RESULTS_FILE = OUTPUT_DIR / "results.md"
RESULTS_FILE_SUMMARIZED = OUTPUT_DIR / "results_comic.md"


# Ensure output dir exists
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Load workflow
with open(WORKFLOW_PATH) as f:
    raw = json.load(f)
    # Ensure correct format for ComfyUI API
    base_workflow = raw if "prompt" in raw else {"prompt": raw}

# Setup logging
if not LOG_FILE.exists():
    with open(LOG_FILE, "w", newline="") as log:
        writer = csv.writer(log)
        writer.writerow(["timestamp", "panel_number", "variation", "seed", "prompt", "output_path"])

# Setup results md
if not RESULTS_FILE.exists():
    with open(RESULTS_FILE, "a") as md:
        md.write(f"# IS A HOTDOG 🌭 A SANDWICH 🥪 TALE! \n")
        # md.write(f"##")
        md.write(f"**File Used**: `{str(CSV_PATH).split('/')[-1]}`\n\n\n")

        # New section introducing the characters
        md.write("## Introducing the key characters:\n\n")

        md.write("***The Hotdog!🌭***\n\n")
        md.write("![hotdog_intro.webp](/inputs/reference_images/hotdog_intro.webp)\n\n")

        md.write("***The Data Scientist👩‍💻***\n\n")
        md.write("![datascientist_entry.webp](/inputs/reference_images/datascientist_entry.webp)\n\n")

        # Start of story
        md.write("## And, The story begins!\n")

# Setup results md
if not RESULTS_FILE_SUMMARIZED.exists():
    with open(RESULTS_FILE_SUMMARIZED, "a") as md:
        md.write(f"# IS A HOTDOG 🌭 A SANDWICH 🥪 TALE! \n")
        # md.write(f"##")
        md.write(f"- **File Used**: `{str(CSV_PATH).split('/')[-1]}`\n")

        # New section introducing the characters
        md.write("## Introducing the key characters:\n\n")

        md.write("***The Hotdog!🌭***\n\n")
        md.write("![hotdog_intro.webp](/inputs/reference_images/hotdog_intro.webp)\n\n")

        md.write("***The Data Scientist👩‍💻***\n\n")
        md.write("![datascientist_entry.webp](/inputs/reference_images/datascientist_entry.webp)\n\n")

        # Start of story
        md.write("## And, The story begins!\n")

def update_prompt(workflow_data, prompt_text):
    """
    Inject the prompt text into CLIPTextEncode node in the workflow.
    """
    for node in workflow_data["prompt"].values():
        if node["class_type"] == "CLIPTextEncode":
            node["inputs"]["text"] = prompt_text
    return workflow_data

def inject_seed(workflow_data, seed):
    """
    Update seed values for any node that accepts seed.
    """
    for node in workflow_data["prompt"].values():
        if "seed" in node.get("inputs", {}):
            node["inputs"]["seed"] = seed
    return workflow_data

def send_to_comfyui(prompt_text, panel_num, variation, counter, seed):
    # seed = random.randint(0, 2**32 - 1)

    
    # Clone and modify workflow
    workflow_copy = json.loads(json.dumps(base_workflow))  # Deep copy
    workflow_copy = update_prompt(workflow_copy, prompt_text)
    workflow_copy = inject_seed(workflow_copy, seed)
    steps = extract_steps_from_workflow(workflow_copy)

    filename = f"panel_{panel_num}_v{variation}_{counter}_.png"
    workflow_copy = set_filename_prefix(workflow_copy, f"panel_{panel_num}_v{variation}", OUTPUT_DIR)


    # Send to ComfyUI API
    response = requests.post(f"{COMFY_API}/prompt", json=workflow_copy)

    if response.status_code != 200:
        print(f"❌ API error: {response.status_code} - {response.text}")
        return



    
    print(f"✅ Sent to ComfyUI: Panel {panel_num}, Variation {variation}, Filename {filename}")
    print(f"🖼️ Image expected at: {OUTPUT_DIR / filename}")


    # ✅ Append markdown log
    append_to_markdown(prompt_text, seed, steps, filename)

    # Log
    with open(LOG_FILE, "a", newline="") as log:
        writer = csv.writer(log)
        writer.writerow([
            datetime.now().isoformat(),
            panel_num,
            variation,
            seed,
            prompt_text,
            filename
            # f"panel_{panel_num}_v{variation}.png"
        ])

def generate_panels():
    print(f"📖 Reading CSV: {CSV_PATH}")
    with open(CSV_PATH) as f:
        reader = csv.DictReader(f)
        for row in reader:
            panel_num = row["panel_number"].strip()
            desc = row["description"].strip()
            chars = row["characters"].strip()
            prompt = f"{desc}. {chars}, manga style, vibrant colors"
            # seed = int(row["seed"]) if "seed" in row and row["seed"].strip() else random.randint(0, 2**32 - 1)
            seed = 747632286252745

            counter = 1
            for i in range(1, 2):  # 5 variations
                
                send_to_comfyui(prompt, panel_num, i, f"{counter:05d}", seed)
                counter = counter + 1

def append_to_markdown(prompt_text, seed, steps, filename):
    # markdown_path = OUTPUT_DIR / "results.md"
    with open(RESULTS_FILE, "a") as md:
        md.write(f"### 🖼️ `{filename}`\n")
        md.write(f"- **Prompt**: `{prompt_text}`\n")
        md.write(f"- **Seed**: `{seed}`\n")
        md.write(f"- **Steps**: `{steps}`\n")
        md.write(f"- **Output**: `{filename}`\n")
        # md.write(f"{OUTPUT_DIR / filename}")
        md.write(f"![{filename}](/outputs/{OUTPUT_FOLDER}/{filename})\n\n")
        # md.write(f"![{filename}](/outputs/{filename})\n\n")
        # md.write(f"![{filename}](/teamspace/studios/this_studio/ComfyUI/outputs/{filename})\n\n")


    # writing to the summarized output manga comic markdown results file
    with open(RESULTS_FILE_SUMMARIZED, "a") as md:
        # md.write(f"### 🖼️ `{filename}`\n")
        # md.write(f"- **Prompt**: `{prompt_text}`\n")
        # md.write(f"- **Seed**: `{seed}`\n")
        # md.write(f"- **Steps**: `{steps}`\n")
        # md.write(f"- **Output**: `{filename}`\n")
        # md.write(f"{OUTPUT_DIR / filename}")
        md.write(f"![{filename}](/outputs/{OUTPUT_FOLDER}/{filename})\n\n")


    

def set_filename_prefix(workflow_data, prefix, folder):
    for node in workflow_data["prompt"].values():
        if node["class_type"] == "SaveImageKJ":
            node["inputs"]["filename_prefix"] = prefix
            node["inputs"]["output_folder"] = str(folder)  # << Inject the full output path here

    return workflow_data

def extract_steps_from_workflow(workflow_data):
    for node in workflow_data["prompt"].values():
        if node["class_type"] == "KSampler":
            return node["inputs"].get("steps", 20)  # fallback to 20
    return 20

if __name__ == "__main__":
    print("⚡ Starting panel generation using ComfyUI API...")
    generate_panels()
    print("🎉 Done! Check output logs in:", LOG_FILE)

    # Adding Ending lines
    # if not RESULTS_FILE.exists():
    with open(RESULTS_FILE, "a") as md:
        # Last Scene
        md.write("## Let's celebrate\n\n")
        md.write("![hotdog_victory2.webp](/inputs/reference_images/hotdog_victory2.webp)\n\n")


    # Setup results md
    # if not RESULTS_FILE_SUMMARIZED.exists():
    with open(RESULTS_FILE_SUMMARIZED, "a") as md:
            # Last Scene
            md.write("## Let's celebrate\n\n")
            md.write("![hotdog_victory2.webp](/inputs/reference_images/hotdog_victory2.webp)\n\n")
