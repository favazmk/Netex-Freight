with open('c:/Users/favaz/Netex-Freight/Netex-Freigh/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

start_idx = -1
end_idx = -1
for i, line in enumerate(lines):
    if '<!-- HERO FLOATING BADGES ROW -->' in line:
        start_idx = i
    if start_idx != -1 and '<!-- CORPORATE PROFILE / ABOUT NETEX SECTION -->' in line:
        end_idx = i - 2
        break

badges_lines = lines[start_idx:end_idx]
del lines[start_idx:end_idx]

insert_idx = -1
for i, line in enumerate(lines):
    if '<!-- MAJESTIC LOGISTICS HERO BLOCK -->' in line:
        insert_idx = i
        break

lines = lines[:insert_idx] + badges_lines + lines[insert_idx:]

for i, line in enumerate(lines):
    if '<!-- MAJESTIC LOGISTICS HERO BLOCK -->' in line:
        if '<section id="hero"' in lines[i+1]:
            lines[i+1] = lines[i+1].replace('bg-transparent', 'bg-zinc-50')
            break

with open('c:/Users/favaz/Netex-Freight/Netex-Freigh/index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)
