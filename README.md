# the-sandwich-trial


# 🌭 The Trial of the Century: Is a Hotdog a Sandwich?

Welcome to *Sizzle Buns*—a playful, data-driven storytelling project where a humble hotdog fights for its identity in a food court of law.

## 🧑‍⚖️ Project Overview

This project transforms public opinion into an absurd yet insightful courtroom drama, using real survey responses to determine one thing:  
**Is a hotdog a sandwich?**

I analyzed data from 500+ participants, extracted demographic and sentiment insights, and built an automated AI pipeline that turns structured data (like a CSV) into manga-style comic panels. Each character—from Judge Sandwich to rebellious Taco—is backed by actual survey logic.

![image](https://github.com/user-attachments/assets/52684742-ab69-4de3-8820-55ef2963c1c9)

It’s data. It’s drama. It’s deliciously absurd.

## 🎯 Goal

To showcase how data science and creative storytelling can merge into something both visually compelling and insight-rich. The project pipeline enables anyone to take a CSV file and generate their own comic-style visual story using editable prompts, styles, and scenes—no design skills required.

## 🛠️ Features

- 🔍 **Insight Extraction**: Analyzes numeric, categorical, and sentiment-based survey data  
- 📊 **Visualization**: Generates charts and personas from demographic trends  
- 🖼️ **Automated Comic Generation**: Converts rows in a CSV into AI-generated story panels  
- 🎨 **Customizable Workflow**: Modify style, characters, and narrative directly through CSV inputs  
- 🚀 **Reusable Pipeline**: Designed to work with any structured dataset (not just hotdogs!)  
- 🛠️ **Future Enhancements**:
  - Text correction in generated images  
  - In-image editing & character tracking  
  - Video generation using the same CSV-first logic

## 📂 Repository Structure

```
📁 /project
├── data/
│   └── cleaned_survey_data.csv
├── notebook/
│   └── HotdogSandwichResearch.ipynb
├── scripts/
│   └── generate_comic.py
├── assets/
│   └── comic_panels/
├── comfyui_workflows/
│   └── hotdog_comic_workflow.json
└── README.md
```

## 🧪 How to Use


1. Clone the repo and upload your structured dataset (CSV format).
2. Update the `generate_comic.py` script or ComfyUI workflow with your desired prompt structure.
3. Run the workflow to generate panels using your GPU-enabled instance.
4. Enjoy your auto-generated comic, based on real data!

> Want to turn a customer feedback CSV into a sci-fi comic? You can.  
> Want to visualize quarterly earnings as a soap opera? That too.  

## 🧰 Tech Stack

- **Python** (Pandas, NumPy, Seaborn, Matplotlib) – for data prep & EDA  
- **Google Colab** – for analysis and reproducibility  
- **ComfyUI** – for node-based image generation  
- **Flex Schnell SDXL + CLIP Text Encoder** – via HuggingFace  
- **Hunyuan** – (planned) for text-to-video capabilities  
- **ChatGPT** – for story planning and creative scaffolding  
- **Notion** – for scripting, visual layout, and planning  

## 📽️ Demo
  
📊 [Google Colab Notebook](https://colab.research.google.com/drive/1d9hQfvacyidD5hrHqp2Row-M_DRT6UB5?usp=sharing)

🎨 [Sample Comic Panel - Using CHATGPT](https://generated-mantis-1f3.notion.site/Comic-1d5b1b47f1c18052abc1e627f1b7eaef)

🎨 [Sample Comic Panel - Using Open Source Flux and Hunyuan Models](https://github.com/raikwarswati/the-sandwich-trial/blob/main/manga_panels_manual/results_comic.md)



---

## 🤝 Credits

Created with ❤️ by Swathi Raikwar  
Part of the [**VanAI Hackathon 2025**](https://kriskrug.notion.site/Data-Storytelling-Hackathon-1a6c6f799a338025bc50d6fc6e9984ae) 
Sponsors of Hackathon [Rival Technologies](https://www.rivaltech.com/?utm_source=google&utm_medium=search&utm_campaign=Branded&utm_content=RivalTech&utm_term=rival%20technologies&utm_campaign=%5B2L%5D+Branded&utm_source=adwords&utm_medium=ppc&hsa_acc=1677755548&hsa_cam=21041600835&hsa_grp=161643268520&hsa_ad=691704104307&hsa_src=g&hsa_tgt=kwd-1532023863836&hsa_kw=rival%20technologies&hsa_mt=e&hsa_net=adwords&hsa_ver=3&gad_source=1&gclid=Cj0KCQjwzYLABhD4ARIsALySuCRweHxNcn8G1_b_hVYorwdiQFOnnNA2VSOApxa1lF3rcPIlSwJV9OIaAuPsEALw_wcB)

GitHub: [@swatyraikwar](https://github.com/swatyraikwar)

---

## 💡 License

MIT License — feel free to remix, adapt, and build your own data-powered drama!
