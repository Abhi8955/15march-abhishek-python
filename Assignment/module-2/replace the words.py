def not_poor_replace(s):
    not_idx = s.find('not')
    poor_idx = s.find('poor')
    if not_idx != -1 and poor_idx != -1 and not_idx < poor_idx:
        return s[:not_idx] + 'good' + s[poor_idx+4:]
    else:
        return s
