import re

with open('C:/Users/ajayc/Downloads/portfolio1/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

def replace_between(text, start_marker, end_marker, new_content):
    pattern = re.escape(start_marker) + r'.*?' + re.escape(end_marker)
    replacement = start_marker + '\n' + new_content + '\n' + end_marker
    return re.sub(pattern, replacement, text, flags=re.DOTALL)

projects_html = '''      <a class="project-item reveal" href="https://github.com/Ajaychinthakindi" target="_blank">
        <span class="project-num">01 —</span>
        <div>
          <div class="project-name">Smart Agriculture Support System (Crop Recommendation + Soil Analysis)</div>
          <p class="project-desc" style="margin-bottom: 0.5rem; display: list-item; list-style-type: disc; margin-left: 1rem;">Developed an intelligent agriculture support system using Machine Learning to analyze soil parameters (pH, NPK, moisture) and environmental factors to recommend the most suitable crop for higher productivity.</p>
          <p class="project-desc" style="margin-bottom: 0.5rem; display: list-item; list-style-type: disc; margin-left: 1rem;">Implemented data preprocessing, soil-quality evaluation, and a crop recommendation engine using Random Forest with a user-friendly dashboard to visualize inputs, and predicted crops.</p>
          <p class="project-desc" style="margin-bottom: 0; display: list-item; list-style-type: disc; margin-left: 1rem;">Achieved 85%-95% accurate crop predictions, provided actionable farming suggestions, and helped reduce crop selection risks-supporting precision agriculture and sustainable farming practices.</p>
        </div>
        <div class="project-meta">
          <div class="project-date">Nov 2025 – Dec 2025</div>
          <div class="project-tags">
            <span class="tag">Machine Learning</span>
            <span class="tag">Random Forest</span>
            <span class="tag">Python</span>
          </div>
        </div>
        <div class="project-arrow">↗</div>
      </a>

      <a class="project-item reveal" href="https://github.com/Ajaychinthakindi" target="_blank">
        <span class="project-num">02 —</span>
        <div>
          <div class="project-name">AI-Powered Traffic Violation Detection System</div>
          <p class="project-desc" style="margin-bottom: 0.5rem; display: list-item; list-style-type: disc; margin-left: 1rem;">Developed an AI-powered Traffic Violation Detection System using YOLO and OpenCV to automatically detect No-helmet riding, triple riding, signal jumping, and number plate extraction.</p>
          <p class="project-desc" style="margin-bottom: 0.5rem; display: list-item; list-style-type: disc; margin-left: 1rem;">Implemented real-time object detection, violation classification, and Automated Number Plate Recognition (ANPR) using Tesseract OCR and Python.</p>
          <p class="project-desc" style="margin-bottom: 0; display: list-item; list-style-type: disc; margin-left: 1rem;">Generated automated violation reports with 85-95% accuracy, enabling faster enforcement and supporting smart City traffic monitoring.</p>
        </div>
        <div class="project-meta">
          <div class="project-date">Nov 2025 – Dec 2025</div>
          <div class="project-tags">
            <span class="tag">Python</span>
            <span class="tag">YOLO</span>
            <span class="tag">OpenCV</span>
            <span class="tag">Tesseract OCR</span>
          </div>
        </div>
        <div class="project-arrow">↗</div>
      </a>'''

html = replace_between(html, '<div class="project-list">', '</div>\n    <div class="view-more-wrap">', projects_html)

# Wait, the view-more-wrap was removed in the previous script!
# So the end_marker is just '    </section>' for the work section
html = replace_between(html, '<div class="project-list">', '</section>', projects_html + '\n    </div>\n  ')

with open('C:/Users/ajayc/Downloads/portfolio1/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
