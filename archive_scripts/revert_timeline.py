import re

with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# The start marker of our injected block
start_marker = '<div id="about-page-workflow-timeline" class="w-full mt-10">'
end_marker = '</div>\n          </div>\n        </section>'

start_idx = html_content.find(start_marker)
if start_idx != -1:
    # Find the next closing of the section
    end_idx = html_content.find(end_marker, start_idx)
    if end_idx != -1:
        # Revert to the original empty placeholder
        original_placeholder = '            <div class="relative border-l border-zinc-200 md:border-l-0 md:grid md:grid-cols-5 md:gap-6 pl-4 md:pl-0 space-y-8 md:space-y-0" id="about-page-workflow-timeline">\n              <!-- Generated dynamically by JS -->\n            </div>'
        new_html = html_content[:start_idx] + original_placeholder + '\n          </div>\n        </section>' + html_content[end_idx + len(end_marker):]
        
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_html)
        print("Successfully reverted index.html")
    else:
        print("End marker not found")
else:
    print("Start marker not found")
