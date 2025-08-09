# Github-Art 🎨  

Create pixel-style artwork in your GitHub contribution graph using a lightweight Python script.  

---

## 📌 Overview  

### 💡 Why This Project Exists  
Because it’s fun! In the developer world, many take pride in their wall of green squares on GitHub.  
So why not use that as a creative canvas?  

The GitHub contributions grid is a **52 x 7 pixel canvas** — perfect for making your profile stand out with shapes, patterns, or even words.  
This project lets you turn your commit history into art.  

### ⚙️ How It Works  
You design a **matrix** where:  
- `#` = make a commit (pixel filled)  
- `.` = leave blank (pixel empty)  

The script creates commits that correspond to your design, which then shows up in your GitHub contribution chart.  

---

## 🖼 Example Pixel Art  

Here’s a simple “HI” example:  

##..##..###..##
##..##...##.##
######....####
##..##...##.##
##..##..###..##


---

## 🚀 Usage  

1. **Fork This Repo**  
   Click **Fork** to copy this repository to your own GitHub account.  

2. **Clone the Repo**  
   ```bash
   git clone https://github.com/INSANE0777/Commit-Art.git           

    Design Your Pixel Art
    Open the script and replace the default matrix with your own # and . pattern.
                          
    Run the Script

        Install the required package:

pip install pillow

Generate the commits:

    python generate_commits.py

Push to GitHub

    git push origin main

✅ Your custom design will now appear on your GitHub profile's contribution graph.
📦 Requirements

    Python 3.x

    Pillow library

⚠️ Disclaimer

This project is for educational and creative purposes only.
Do not abuse it to artificially inflate commit counts — this can violate GitHub’s Terms of Service.
Keep it fun, responsible, and artistic.
📄 License

Licensed under the Apache-2.0 License.
See the LICENSE file for details.


If you want, I can also make **an ASCII pixel art GitHub logo** as the default matrix in the README so 