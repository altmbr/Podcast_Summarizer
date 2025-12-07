---
name: gmail-email-html
description: Best practices for HTML email formatting that works reliably in Gmail and other email clients, including layout patterns, CSS restrictions, and compatibility fixes
---

# Gmail Email HTML Best Practices

Expert guidance for building HTML emails that render correctly in Gmail and other email clients.

## Critical Patterns

### 1. Container Structure
- **Use table-based layouts for main containers with borders**
  - Gmail handles table borders more reliably than div borders
  - Structure: `<table><tr><td style="border: 3px solid #000;">content</td></tr></table>`
  - Avoid: `<div style="border: 3px solid #000;">content</div>` for critical bordered containers

### 2. Text Elements Inside Tables
- **Use `<div>` tags instead of `<p>` tags inside table cells**
  - Problem: Gmail may break `<p>` tags out of `<td>` elements
  - Solution: Replace all `<p>` with `<div>` inside table cells
  - Safe: Nested divs are more reliable than paragraphs

### 3. CSS Restrictions in Gmail
- **NEVER use `box-shadow`** - Gmail doesn't support it and it breaks container boundaries
  - Symptom: Content appears outside bordered boxes
  - Source: caniemail.com, Stack Overflow debugging

- **NEVER use `display: block` on `<td>` elements** - causes layout breaks

- **Avoid `display: inline-block`** on elements that need to work when forwarded
  - Forwarding breaks inline-block rendering
  - Use simple block or inline elements instead

### 4. All CSS Must Be Inline
- No `<style>` tags in `<head>`
- No external stylesheets
- All styling via `style=""` attributes

### 5. Email Client Safe Patterns
```html
<!-- GOOD: Table-based bordered container -->
<table width="100%" cellpadding="0" cellspacing="0" border="0">
    <tr>
        <td style="background: #fff; padding: 32px; border: 3px solid #000;">
            <!-- Content here -->
            <div style="text-align: center; margin-bottom: 16px;">
                Footer text
            </div>
        </td>
    </tr>
</table>

<!-- BAD: Div-based with box-shadow -->
<div style="border: 3px solid #000; box-shadow: 4px 4px 0 #000;">
    <p style="margin: 0;">Footer text</p>  <!-- May break out in Gmail -->
</div>
```

## Debugging Checklist

When content appears outside bordered containers:
1. ✓ Check for `box-shadow` - remove it
2. ✓ Replace `<p>` tags with `<div>` inside `<td>`
3. ✓ Convert div-based borders to table-based structure
4. ✓ Verify all CSS is inline
5. ✓ Test forwarding (inline-block breaks on forward)

## Email Client Compatibility

| Feature | Gmail | Outlook | Apple Mail |
|---------|-------|---------|------------|
| `box-shadow` | ❌ | ✓ | ✓ |
| `<p>` in `<td>` | ⚠️ Unreliable | ✓ | ✓ |
| Table borders | ✓ | ✓ | ✓ |
| Inline styles | ✓ | ✓ | ✓ |

## Real-World Example

This skill was created after debugging a Daily Teahose newsletter where the unsubscribe footer kept appearing outside the bordered email card in Gmail.

**Solution that worked:**
- Main container: table with border on `<td>`
- Footer: nested `<div>` tags (not `<p>`)
- No `box-shadow` anywhere
- All content inside the `<td>` element

## References
- caniemail.com - Email client CSS support
- Stack Overflow: Gmail email rendering issues
- Tested in: Gmail web, Gmail mobile, Apple Mail, Outlook
