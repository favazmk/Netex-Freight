def strip_hover_media(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        css = f.read()

    out = []
    i = 0
    while i < len(css):
        if css[i:].startswith('@media (hover: hover)'):
            # find the opening brace
            brace_idx = css.find('{', i)
            i = brace_idx + 1
            
            brace_count = 1
            inner_content = []
            while i < len(css) and brace_count > 0:
                if css[i] == '{':
                    brace_count += 1
                elif css[i] == '}':
                    brace_count -= 1
                
                if brace_count > 0:
                    inner_content.append(css[i])
                i += 1
            out.append("".join(inner_content))
        else:
            out.append(css[i])
            i += 1

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("".join(out))

strip_hover_media('src/style.css')
print("Successfully removed @media (hover: hover) wrappers.")
