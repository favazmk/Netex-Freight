import re

with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

with open('infographic.html', 'r', encoding='utf-8') as f:
    new_timeline = f.read()

# Replace everything from <div ... id="about-page-workflow-timeline"> to its closing </div>
# using regex or string splitting

start_marker = '            <div class="relative border-l border-zinc-200 md:border-l-0 md:grid md:grid-cols-5 md:gap-6 pl-4 md:pl-0 space-y-8 md:space-y-0" id="about-page-workflow-timeline">'
end_marker = '            </div>\n          </div>\n        </section>'

start_idx = html_content.find(start_marker)
if start_idx != -1:
    end_idx = html_content.find(end_marker, start_idx)
    if end_idx != -1:
        # Wrap new_timeline in the id container
        replacement = f'<div id="about-page-workflow-timeline" class="w-full mt-10">\n{new_timeline}\n            </div>'
        new_html = html_content[:start_idx] + replacement + '\n          </div>\n        </section>' + html_content[end_idx + len(end_marker):]
        
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_html)
        print("Successfully replaced.")
    else:
        print("End marker not found")
else:
    print("Start marker not found")
