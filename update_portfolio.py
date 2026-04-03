import re

with open('C:/Users/ajayc/Downloads/portfolio1/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

def replace_between(text, start_marker, end_marker, new_content):
    pattern = re.escape(start_marker) + r'.*?' + re.escape(end_marker)
    replacement = start_marker + '\n' + new_content + '\n' + end_marker
    return re.sub(pattern, replacement, text, flags=re.DOTALL)

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
        <span class="skill-pill cat">Frameworks</span>
        <span class="skill-pill">HTML</span>
        <span class="skill-pill">CSS</span>
        <span class="skill-pill cat">Languages</span>
        <span class="skill-pill">C</span>
        <span class="skill-pill">C++</span>
        <span class="skill-pill">Java</span>
        <span class="skill-pill">Python</span>
        <span class="skill-pill cat">Frameworks</span>
        <span class="skill-pill">HTML</span>
        <span class="skill-pill">CSS</span>
      </div>
      <div class="skills-row row-2">
        <span class="skill-pill cat">Tools & Platforms</span>
        <span class="skill-pill">MySQL</span>
        <span class="skill-pill">Git & GitHub</span>
        <span class="skill-pill">VS Code</span>
        <span class="skill-pill">Selenium</span>
        <span class="skill-pill">TestNG</span>
        <span class="skill-pill">JUnit</span>
        <span class="skill-pill cat">Tools & Platforms</span>
        <span class="skill-pill">MySQL</span>
        <span class="skill-pill">Git & GitHub</span>
        <span class="skill-pill">VS Code</span>
        <span class="skill-pill">Selenium</span>
        <span class="skill-pill">TestNG</span>
        <span class="skill-pill">JUnit</span>
      </div>
      <div class="skills-row row-3">
        <span class="skill-pill cat">Soft Skills</span>
        <span class="skill-pill">Problem-Solving</span>
        <span class="skill-pill">Team Player</span>
        <span class="skill-pill">Leadership</span>
        <span class="skill-pill">Adaptability</span>
        <span class="skill-pill cat">Soft Skills</span>
        <span class="skill-pill">Problem-Solving</span>
        <span class="skill-pill">Team Player</span>
        <span class="skill-pill">Leadership</span>
        <span class="skill-pill">Adaptability</span>
        <span class="skill-pill cat">Soft Skills</span>
        <span class="skill-pill">Problem-Solving</span>
        <span class="skill-pill">Team Player</span>
        <span class="skill-pill">Leadership</span>
        <span class="skill-pill">Adaptability</span>
      </div>
    </div>'''

html = replace_between(html, '<section class="skills" id="skills">', '</section>', skills_html)

training_html = '''    <div class="section-label reveal">Training</div>
    <div class="training-list">
      <div class="training-card reveal">
        <div class="training-card-top">
          <div class="training-card-left">
            <span class="training-badge">&#9670; Summer Training</span>
            <div class="training-name">C++ & Data Structures</div>
            <div class="training-org">Cipher Schools</div>
          </div>
          <div class="training-period-box">Jun 2025 – Jul 2025</div>
        </div>
        <div class="training-divider"></div>
        <ul style="color: var(--muted); padding-left: 1.5rem; margin-bottom: 1.5rem; line-height: 1.8;">
          <li>Completed an intensive summer Training Program in C++ and Data Structures, strengthening Programming, Fundamental and problem-solving skills through hands-on implementation.</li>
          <li>Gained practical expertise in arrays, linked lists, stacks, queues, trees, and searching & sorting algorithms, Improving algorithmic efficiency and logical optimization capabilities by 70%.</li>
          <li>Developed multiple DSA-based programs and mini-projects using OOP principles, enhancing code Structuring, debugging skills, and execution performance by 65%.</li>
        </ul>
        <div class="training-footer">
          <div class="training-tags">
            <span class="training-tag">C++</span>
            <span class="training-tag">DSA</span>
            <span class="training-tag">OOP</span>
            <span class="training-tag">Algorithms</span>
          </div>
        </div>
      </div>
    </div>'''

html = replace_between(html, '<section class="training" id="training">', '</section>', training_html)

certs_html = '''    <div class="section-label reveal">Certificates</div>
    <div class="certs-list">
      <div class="cert-row reveal">
        <div class="cert-info" style="width: 100%;">
          <div class="cert-platform">Cipher Schools</div>
          <div class="cert-name">Summer Training in C++ & Data Structures</div>
          <div class="cert-date">July 2025</div>
        </div>
      </div>
      <div class="cert-row reveal">
        <div class="cert-info" style="width: 100%;">
          <div class="cert-platform">Infosys Springboard</div>
          <div class="cert-name">Computational Theory: Language Principle and automata Theory</div>
          <div class="cert-date">August 2025</div>
        </div>
      </div>
      <div class="cert-row reveal">
        <div class="cert-info" style="width: 100%;">
          <div class="cert-platform">Coursera</div>
          <div class="cert-name">Computer Communications Specialization</div>
          <div class="cert-date">2025</div>
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
          <div class="edu-loc">Punjab, India</div>
          <span class="edu-score">CGPA: 6.5</span>
        </div>
      </div>
      <div class="edu-item">
        <div class="edu-years">Jun 2021 – Mar 2023</div>
        <div class="edu-card">
          <div class="edu-degree">Intermediate - MPC</div>
          <div class="edu-school">Vikas Junior College</div>
          <div class="edu-loc">Peddapalli, Telangana</div>
          <span class="edu-score">84%</span>
        </div>
      </div>
      <div class="edu-item">
        <div class="edu-years">Jun 2020 – Mar 2021</div>
        <div class="edu-card">
          <div class="edu-degree">Matriculation</div>
          <div class="edu-school">ZPHS Jayyaram</div>
          <div class="edu-loc">Jayyaram, Telangana</div>
          <span class="edu-score">100%</span>
        </div>
      </div>
    </div>'''

html = replace_between(html, '<section class="education" id="education">', '</section>', edu_html)

ach_html = '''    <div class="section-label reveal">Recognition</div>
    <div class="ach-grid">
      <div class="ach-card reveal">
        <div class="ach-card-top">
          <span class="ach-badge">&#127881; Problem Solving</span>
          <div class="ach-rank">100+</div>
        </div>
        <div class="ach-title">100+ Problems Solved</div>
        <p class="ach-desc">Solved 100+ problems across platforms like LeetCode and GeeksforGeeks, strengthening problem-solving and algorithmic thinking skills.</p>
        <div class="ach-footer">
          <div class="ach-date">April 2025</div>
          <div class="ach-scope">LPU</div>
        </div>
      </div>
      <div class="ach-card reveal reveal-delay-1">
        <div class="ach-card-top">
          <span class="ach-badge">&#127942; Hackathon</span>
          <div class="ach-rank">#8</div>
        </div>
        <div class="ach-title">8th Position — University Hackathon</div>
        <p class="ach-desc">Secured 8th Position among 200+ Teams in a university-level hackathon focused on innovation &amp; problem solving.</p>
        <div class="ach-footer">
          <div class="ach-date">Nov 2025</div>
          <div class="ach-scope">University Level</div>
        </div>
      </div>
    </div>'''

html = replace_between(html, '<section class="achievements" id="achievements">', '</section>', ach_html)

# Clean up modals and buttons that we don't need
html = replace_between(html, '<!-- PROJECTS MODAL -->', '</div>\n  </div>', '')
html = replace_between(html, '<!-- CERTIFICATES MODAL -->', '</div>\n  </div>', '')
# Remove view more projects button
html = html.replace('<div class="view-more-wrap">\n      <button class="view-more-btn" id="viewMoreBtn">More Projects <span>+</span></button>\n    </div>', '')
# Remove view more certs button 
html = html.replace('<div class="view-more-wrap" style="background:var(--navy);">\n      <button class="view-more-btn" id="viewMoreCertsBtn">More Certificates <span>+</span></button>\n    </div>', '')

# Replace footer text
html = html.replace('© 2026 Velagapudi Sai Tanmai', '© 2026 Ajay Chinthakindi')

with open('C:/Users/ajayc/Downloads/portfolio1/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
