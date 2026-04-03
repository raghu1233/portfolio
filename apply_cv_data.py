import re

with open(r'C:\Users\ajayc\Downloads\raghu portfolio\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

def replace_between(text, start_marker, end_marker, new_content):
    pattern = re.escape(start_marker) + r'.*?' + re.escape(end_marker)
    replacement = start_marker + '\n' + new_content + '\n' + end_marker
    return re.sub(pattern, replacement, text, flags=re.DOTALL)

# Header Updates (Bio and Links)
html = html.replace('linkedin.com/in/chinthakindi-ajay-980244283/', 'linkedin.com/in/raghuram6/')
html = html.replace('github.com/Ajaychinthakindi', 'github.com/raghu1233')
html = html.replace('B.Tech CSE student passionate about building intelligent systems, data-driven applications, and exploring the intersection of AI and real-world problem solving.', 'Computer Science student passionate about Web Development, QA Automation, and sustainable solutions. Skilled in automated testing, full-stack design, and team collaboration.')

skills_html = '''    <div class="skills-header">
      <div class="section-label reveal">Capabilities</div>
    </div>
    <div class="skills-track-wrap">
      <div class="skills-row row-1">
        <span class="skill-pill cat">Languages</span>
        <span class="skill-pill">C</span>
        <span class="skill-pill">C++</span>
        <span class="skill-pill">Java</span>
        <span class="skill-pill">Python</span>
        <span class="skill-pill">JavaScript</span>
        <span class="skill-pill">SQL</span>
        <span class="skill-pill cat">Frameworks</span>
        <span class="skill-pill">HTML</span>
        <span class="skill-pill">CSS</span>
        <span class="skill-pill">Selenium</span>
        <span class="skill-pill">PyTest</span>
        <span class="skill-pill">TestNG</span>
        <span class="skill-pill">CyPress</span>
        <span class="skill-pill cat">Languages</span>
        <span class="skill-pill">C</span>
        <span class="skill-pill">C++</span>
        <span class="skill-pill">Java</span>
        <span class="skill-pill">Python</span>
        <span class="skill-pill">JavaScript</span>
        <span class="skill-pill">SQL</span>
      </div>
      <div class="skills-row row-2">
        <span class="skill-pill cat">Tools & Platforms</span>
        <span class="skill-pill">Jira</span>
        <span class="skill-pill">JMeter</span>
        <span class="skill-pill">K6</span>
        <span class="skill-pill">Testrail</span>
        <span class="skill-pill">GitHub</span>
        <span class="skill-pill">Appium</span>
        <span class="skill-pill">SoapUI</span>
        <span class="skill-pill cat">Tools & Platforms</span>
        <span class="skill-pill">Jira</span>
        <span class="skill-pill">JMeter</span>
        <span class="skill-pill">K6</span>
        <span class="skill-pill">Testrail</span>
        <span class="skill-pill">GitHub</span>
        <span class="skill-pill">Appium</span>
        <span class="skill-pill">SoapUI</span>
      </div>
      <div class="skills-row row-3">
        <span class="skill-pill cat">Soft Skills</span>
        <span class="skill-pill">Leadership</span>
        <span class="skill-pill">Problem Solving</span>
        <span class="skill-pill">Adaptability</span>
        <span class="skill-pill">Time Management</span>
        <span class="skill-pill cat">Soft Skills</span>
        <span class="skill-pill">Leadership</span>
        <span class="skill-pill">Problem Solving</span>
        <span class="skill-pill">Adaptability</span>
        <span class="skill-pill">Time Management</span>
        <span class="skill-pill cat">Soft Skills</span>
        <span class="skill-pill">Leadership</span>
        <span class="skill-pill">Problem Solving</span>
      </div>
    </div>'''

html = replace_between(html, '<section class="skills" id="skills">', '</section>', skills_html)

training_html = '''    <div class="section-label reveal">Training</div>
    <div class="training-list">
      <div class="training-card reveal">
        <div class="training-card-top">
          <div class="training-card-left">
            <span class="training-badge">&#9670; Certificate Training</span>
            <div class="training-name">Data Analytics Essentials</div>
            <div class="training-org">Online Platform</div>
          </div>
          <div class="training-period-box">Jun 2025 – Jul 2025</div>
        </div>
        <div class="training-divider"></div>
        <ul style="color: var(--muted); padding-left: 1.5rem; margin-bottom: 1.5rem; line-height: 1.8;">
          <li>Acquired hands-on experience in data analytics tools and techniques, applying Python for programming and analysis, SQL for database management, and Power BI and Tableau for interactive dashboard development.</li>
          <li>Utilized Excel for data preprocessing, cleaning, and summarization, reinforcing its significance in analytics workflows.</li>
        </ul>
        <div class="training-footer">
          <div class="training-tags">
            <span class="training-tag">SQL</span>
            <span class="training-tag">Python</span>
            <span class="training-tag">Power BI</span>
            <span class="training-tag">Tableau</span>
            <span class="training-tag">Excel</span>
          </div>
        </div>
      </div>
    </div>'''

html = replace_between(html, '<section class="training" id="training">', '</section>', training_html)

certs_html = '''    <div class="section-label reveal">Certificates</div>
    <div class="certs-list">
      <div class="cert-row reveal">
        <div class="cert-info" style="width: 100%;">
          <div class="cert-platform">NPTEL</div>
          <div class="cert-name">Cloud Computing</div>
          <div class="cert-date">Jul 2025 – Nov 2025</div>
        </div>
      </div>
      <div class="cert-row reveal">
        <div class="cert-info" style="width: 100%;">
          <div class="cert-platform">Coursera</div>
          <div class="cert-name">TCP/IP and Advanced Topics</div>
          <div class="cert-date">Nov 2024</div>
        </div>
      </div>
      <div class="cert-row reveal">
        <div class="cert-info" style="width: 100%;">
          <div class="cert-platform">Coursera</div>
          <div class="cert-name">The Bits and Bytes of Computer Networking</div>
          <div class="cert-date">Sep 2024</div>
        </div>
      </div>
      <div class="cert-row reveal">
        <div class="cert-info" style="width: 100%;">
          <div class="cert-platform">Coursera</div>
          <div class="cert-name">Introduction to Hardware and Operating Systems</div>
          <div class="cert-date">Sep 2024</div>
        </div>
      </div>
      <div class="cert-row reveal">
        <div class="cert-info" style="width: 100%;">
          <div class="cert-platform">CSE Pathashala</div>
          <div class="cert-name">Mastering C</div>
          <div class="cert-date">Feb 2024 – Mar 2024</div>
        </div>
      </div>
      <div class="cert-row reveal">
        <div class="cert-info" style="width: 100%;">
          <div class="cert-platform">FreeCodeCamp</div>
          <div class="cert-name">Responsive Web Design</div>
          <div class="cert-date">Oct 2023</div>
        </div>
      </div>
    </div>'''

html = replace_between(html, '<section class="certs" id="certs">', '</section>', certs_html)

edu_html = '''    <div class="edu-header">
      <div>
        <div class="section-label reveal">Education</div>
        <h2 class="edu-big reveal reveal-delay-1">Academic<br><em>Journey</em></h2>
      </div>
    </div>
    <div class="edu-timeline reveal">
      <div class="edu-item">
        <div class="edu-years">Aug 2023 – Present</div>
        <div class="edu-card">
          <div class="edu-degree">B.Tech — Computer Science &amp; Engineering</div>
          <div class="edu-school">Lovely Professional University</div>
          <div class="edu-loc">Phagwara, Punjab</div>
          <span class="edu-score">CGPA: 6.49</span>
        </div>
      </div>
      <div class="edu-item">
        <div class="edu-years">Jun 2021 – May 2023</div>
        <div class="edu-card">
          <div class="edu-degree">Intermediate</div>
          <div class="edu-school">Tirumala Junior College</div>
          <div class="edu-loc">Visakhapatnam, Andhra Pradesh</div>
          <span class="edu-score">94.4%</span>
        </div>
      </div>
      <div class="edu-item">
        <div class="edu-years">Jun 2020 – Apr 2021</div>
        <div class="edu-card">
          <div class="edu-degree">Matriculation</div>
          <div class="edu-school">Vijnana Vihara Residential High School</div>
          <div class="edu-loc">Visakhapatnam, Andhra Pradesh</div>
          <span class="edu-score">68%</span>
        </div>
      </div>
    </div>'''

html = replace_between(html, '<section class="education" id="education">', '</section>', edu_html)

ach_html = '''    <div class="section-label reveal">Recognition</div>
    <div class="ach-grid">
      <div class="ach-card reveal">
        <div class="ach-card-top">
          <span class="ach-badge">&#128302; Cyber Security</span>
          <div class="ach-rank">Participant</div>
        </div>
        <div class="ach-title">CyberSec Symposium 2.0</div>
        <p class="ach-desc">Awarded a certificate for diligently attending and being a part of CyberSec Symposium 2.0, North India’s largest Cyber Security Conference, organized by iGen Community.</p>
        <div class="ach-footer">
          <div class="ach-date">Apr 2024</div>
          <div class="ach-scope">LPU</div>
        </div>
      </div>
      <div class="ach-card reveal reveal-delay-1">
        <div class="ach-card-top">
          <span class="ach-badge">&#128150; Volunteer</span>
          <div class="ach-rank">Active</div>
        </div>
        <div class="ach-title">NSS Volunteer</div>
        <p class="ach-desc">Actively participated in community service and social development activities as part of the National Service Scheme (NSS).</p>
        <div class="ach-footer">
          <div class="ach-date">Since Jan 2024</div>
          <div class="ach-scope">Community</div>
        </div>
      </div>
      <div class="ach-card reveal reveal-delay-2">
        <div class="ach-card-top">
          <span class="ach-badge">&#127758; Member</span>
          <div class="ach-rank">Active</div>
        </div>
        <div class="ach-title">NGO Member – Conserve Earth Foundation</div>
        <p class="ach-desc">Actively contributed to environmental awareness and sustainability initiatives as a member of the Conserve Earth Foundation.</p>
        <div class="ach-footer">
          <div class="ach-date">Jul 2024</div>
          <div class="ach-scope">Foundation</div>
        </div>
      </div>
    </div>'''

html = replace_between(html, '<section class="achievements" id="achievements">', '</section>', ach_html)

projects_html = '''      <a class="project-item reveal" href="https://github.com/raghu1233" target="_blank">
        <span class="project-num">01 —</span>
        <div>
          <div class="project-name">Smart Waste Management System</div>
          <p class="project-desc" style="margin-bottom: 0.5rem; display: list-item; list-style-type: disc; margin-left: 1rem;">Developed a Smart Waste Management System using IoT sensors and data analytics to optimize waste collection, reduce operational costs, and promote sustainable practices.</p>
        </div>
        <div class="project-meta">
          <div class="project-date">Jun 2025</div>
          <div class="project-tags">
            <span class="tag">HTML</span>
            <span class="tag">CSS</span>
            <span class="tag">JavaScript</span>
          </div>
        </div>
        <div class="project-arrow">↗</div>
      </a>

      <a class="project-item reveal reveal-delay-1" href="https://github.com/raghu1233" target="_blank">
        <span class="project-num">02 —</span>
        <div>
          <div class="project-name">Saloon and Spa Website</div>
          <p class="project-desc" style="margin-bottom: 0.5rem; display: list-item; list-style-type: disc; margin-left: 1rem;">Developed a modern and responsive Salon & Spa website featuring service listings, pricing, appointment booking, and an elegant UI for enhanced client experience.</p>
        </div>
        <div class="project-meta">
          <div class="project-date">Oct 2024</div>
          <div class="project-tags">
            <span class="tag">HTML</span>
            <span class="tag">CSS</span>
            <span class="tag">JavaScript</span>
          </div>
        </div>
        <div class="project-arrow">↗</div>
      </a>'''

html = replace_between(html, '<div class="project-list">', '</section>', projects_html + '\n    </div>\n  ')

# Clean Footer
html = html.replace('© 2026 Ajay Chinthakindi', '© 2026 Korada Raghu Ram')
html = html.replace('© 2026 Velagapudi Sai Tanmai', '© 2026 Korada Raghu Ram')

with open(r'C:\Users\ajayc\Downloads\raghu portfolio\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("CV Update complete.")
