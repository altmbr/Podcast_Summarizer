---
name: gmail-email-html
description: Best practices for HTML email formatting that works reliably in Gmail and other email clients, including layout patterns, CSS restrictions, and compatibility fixes (project)
---

# HTML Email Best Practices (2025)

Expert guidance for building HTML emails that render correctly across Gmail, Outlook, Apple Mail, and other email clients. Based on industry standards from Mailtrap, Mailchimp, DesignModo, HubSpot, and caniemail.com.

## The Golden Rules

| Rule | Why |
|------|-----|
| **Tables for ALL layout** | Email clients (especially Outlook) use Word's rendering engine, not browser engines. Tables are the only reliable layout method. |
| **600px max width** | Email preview panes are small; 600px is the safe standard, 800px is the upper limit |
| **100% inline CSS** | Gmail strips `<style>` tags and `<head>` content |
| **Avoid CSS shorthand** | Write `padding-top: 10px; padding-right: 10px;` not `padding: 10px` |
| **Double-declare colors** | Use both `bgcolor="#fff"` attribute AND `style="background-color: #fff;"` for maximum compatibility |
| **Full hex codes** | Use `#ffffff` not `#fff` - some clients don't parse shorthand |
| **No JavaScript** | Blocked by all email clients |
| **Keep under 102KB** | Gmail clips larger emails with "View entire message" link |

## CSS Properties to AVOID

| Property | Support | Problem |
|----------|---------|---------|
| `box-shadow` | ~63% | Fails in Outlook Windows, some Gmail configs. Content can escape container boundaries. |
| `display: flex/grid` | ~61% | Breaks in Outlook, older clients |
| `display: inline-block` | Partial | **Breaks when email is forwarded** - use tables instead |
| `position`, `float`, `clear` | Poor | Layout breaks unpredictably |
| `border-radius` | ~85% | Fails in Outlook Windows |
| Web fonts | ~60% | Falls back to system fonts in Gmail/Outlook/Yahoo |

## Required HTML Structure

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="margin: 0; padding: 0; background-color: #f7f4f0;" bgcolor="#f7f4f0">
    <!-- Outer wrapper table for centering -->
    <table width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#f7f4f0" style="background-color: #f7f4f0;">
        <tr>
            <td align="center" style="padding: 20px;">
                <!-- Main content table (600px fixed width) -->
                <table width="600" cellpadding="0" cellspacing="0" border="0" bgcolor="#ffffff" style="background-color: #ffffff; border: 3px solid #1a1a1a; max-width: 600px;">
                    <tr>
                        <td style="padding: 32px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif;">
                            <!-- Content rows go here -->
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
```

## Critical Patterns

### 1. Container Structure - ALWAYS Use Tables
```html
<!-- GOOD: Table-based bordered container -->
<table width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#ffffff" style="background-color: #ffffff; border: 3px solid #000000;">
    <tr>
        <td style="padding: 24px;">
            <div style="font-size: 16px;">Content here</div>
        </td>
    </tr>
</table>

<!-- BAD: Div-based with box-shadow -->
<div style="border: 3px solid #000; box-shadow: 4px 4px 0 #000;">
    <p style="margin: 0;">Content</p>
</div>
```

### 2. Text Elements - Use `<div>` Not `<p>` Inside Tables
```html
<!-- GOOD: Divs inside table cells -->
<td style="padding: 16px;">
    <div style="font-size: 24px; font-weight: bold; margin: 0 0 8px 0;">Title</div>
    <div style="font-size: 14px; color: #555555;">Description</div>
</td>

<!-- BAD: Paragraphs can break out of cells in Gmail -->
<td style="padding: 16px;">
    <p style="font-size: 24px;">Title</p>
    <p style="font-size: 14px;">Description</p>
</td>
```

### 3. Buttons - Table-Based, Not Inline-Block
```html
<!-- GOOD: Table-based button (survives forwarding) -->
<table cellpadding="0" cellspacing="0" border="0" bgcolor="#1a1a1a" style="background-color: #1a1a1a;">
    <tr>
        <td style="padding: 8px 16px; white-space: nowrap;">
            <a href="https://example.com" style="color: #ffffff; text-decoration: none; font-weight: 600; font-size: 14px; white-space: nowrap;">Sign&nbsp;Up</a>
        </td>
    </tr>
</table>

<!-- BAD: Inline-block breaks on forward -->
<a href="https://example.com" style="display: inline-block; background: #1a1a1a; color: #fff; padding: 8px 16px;">Sign Up</a>
```

### 4. Preventing Text Wrap in Buttons
- Use `white-space: nowrap` on the `<td>`, inner elements, AND the `<a>` tag
- Use `&nbsp;` (non-breaking space) between words: `Sign&nbsp;Up`
- This is safe inside table cells (unlike inline-block for layout)

### 5. Images
```html
<!-- Always specify width attribute AND style -->
<img src="image.jpg" width="600" style="width: 100%; max-width: 600px; height: auto; display: block;" alt="Description">
```

### 6. Dividers/Horizontal Rules
```html
<!-- Use table with border-top, not <hr> -->
<table width="100%" cellpadding="0" cellspacing="0" border="0">
    <tr>
        <td style="border-top: 1px solid #555555; padding-bottom: 24px; font-size: 1px; line-height: 1px;">&nbsp;</td>
    </tr>
</table>
```

## Email Client Compatibility Matrix

| Feature | Gmail | Outlook (Windows) | Outlook (Mac/Web) | Apple Mail | Yahoo |
|---------|-------|-------------------|-------------------|------------|-------|
| `box-shadow` | ⚠️ Partial | ❌ | ✓ | ✓ | ✓ |
| `border-radius` | ✓ | ❌ | ✓ | ✓ | ✓ |
| `<p>` in `<td>` | ⚠️ Unreliable | ✓ | ✓ | ✓ | ✓ |
| Table borders | ✓ | ✓ | ✓ | ✓ | ✓ |
| Inline styles | ✓ | ✓ | ✓ | ✓ | ✓ |
| `display: inline-block` | ⚠️ Breaks on forward | ✓ | ✓ | ✓ | ✓ |
| Web fonts | ❌ | ❌ | ❌ | ✓ | ❌ |
| `max-width` | ✓ | ❌ | ✓ | ✓ | ✓ |

## Debugging Checklist

When content appears outside bordered containers or formatting breaks:

1. ✓ Remove all `box-shadow` properties
2. ✓ Replace `<p>` tags with `<div>` inside `<td>` elements
3. ✓ Convert div-based borders to table-based structure
4. ✓ Verify ALL CSS is inline (no `<style>` tags)
5. ✓ Check for `display: inline-block` - replace with table-based buttons
6. ✓ Test forwarding the email (many issues only appear after forward)
7. ✓ Verify full hex codes (`#ffffff` not `#fff`)
8. ✓ Double-check `bgcolor` attributes match `background-color` styles
9. ✓ Ensure email is under 102KB total

## Safe Fonts

Use email-safe fonts with web fallbacks:
```css
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif;
```

Or stick to universally safe fonts:
- Arial, Helvetica (sans-serif)
- Georgia, Times New Roman (serif)
- Courier New (monospace)
- Verdana, Tahoma (sans-serif)

## References

- [caniemail.com](https://www.caniemail.com/) - Email client CSS support database
- [Mailtrap - HTML Email Best Practices](https://mailtrap.io/blog/html-email-best-practices/)
- [Mailchimp - HTML Email Basics](https://templates.mailchimp.com/getting-started/html-email-basics/)
- [DesignModo - HTML and CSS in Emails 2025](https://designmodo.com/html-css-emails/)
- [HubSpot - HTML Email Tables](https://blog.hubspot.com/website/html-email-table)

## Real-World Example

This skill was refined while debugging the Daily Teahose newsletter where:
1. Footer content appeared outside bordered containers (fixed by removing `box-shadow`)
2. "Sign Up" button text wrapped to two lines (fixed with `white-space: nowrap` + `&nbsp;`)
3. Formatting broke when forwarded (fixed by replacing `inline-block` with table-based buttons)

**Final working solution:**
- Outer wrapper table for centering
- Main container: 600px table with border on `<td>`
- All text in `<div>` tags (not `<p>`)
- Buttons as nested tables with `bgcolor` + `background-color`
- No `box-shadow`, no `inline-block`, no `border-radius`
- All content inside the main `<td>` element
