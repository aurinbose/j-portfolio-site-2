# Create the ZIP file with all portfolio files
import zipfile
import io

# Create a ZIP file in memory
zip_buffer = io.BytesIO()

with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
    # Add HTML file
    zip_file.writestr('index.html', html_content)
    
    # Add CSS file  
    zip_file.writestr('style.css', css_content)
    
    # Add JavaScript file
    zip_file.writestr('app.js', js_content)
    
    # Add a README file with instructions
    readme_content = '''# Aurin Bose - Data Analyst Portfolio

## Overview
A modern, professional portfolio website showcasing data analytics expertise and experience.

## Features
- Responsive design for all devices
- Dark theme with blue/teal accents
- Smooth scrolling navigation
- Interactive animations
- Contact form with validation
- Mobile-friendly hamburger menu
- Professional sections: About, Skills, Experience, Projects, Certifications

## Setup Instructions
1. Extract all files to your desired directory
2. Open `index.html` in a web browser
3. For local development, use a local server (Live Server extension in VS Code recommended)

## File Structure
- `index.html` - Main HTML file with all content sections
- `style.css` - Complete CSS styling with responsive design
- `app.js` - JavaScript for interactions and animations
- `README.md` - This file with setup instructions

## Customization
### To add your own photo:
1. Replace the placeholder divs in HTML with `<img>` tags
2. Add your image files to the project directory
3. Update the `src` attributes in the HTML

### To modify colors:
1. Edit the CSS variables in the `:root` section of `style.css`
2. Main colors: `--primary-color`, `--secondary-color`, `--accent-color`

### To update content:
1. Edit the text content directly in `index.html`
2. Update projects, experience, and certifications as needed

## Technologies Used
- HTML5
- CSS3 (Flexbox, Grid, Animations)
- Vanilla JavaScript
- Google Fonts (Inter)

## Browser Support
- Chrome, Firefox, Safari, Edge (modern versions)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Performance
- Optimized images (when added)
- Minimal JavaScript footprint
- CSS animations with reduced motion support
- Responsive design for fast mobile loading

## Contact
For questions about this portfolio template, contact: aurinbose@gmail.com
'''
    
    zip_file.writestr('README.md', readme_content)

# Get the ZIP content
zip_buffer.seek(0)
zip_content = zip_buffer.read()

# Save the ZIP file
with open('aurin-portfolio.zip', 'wb') as f:
    f.write(zip_content)

print("✅ Created aurin-portfolio.zip with the complete portfolio website!")
print("\n📁 Files included:")
print("- index.html (Complete HTML structure)")
print("- style.css (Modern CSS with dark theme)")  
print("- app.js (Interactive JavaScript)")
print("- README.md (Setup instructions)")
print("\n🚀 Ready to use! Extract and open index.html in your browser.")
print("\n📝 Note: Replace placeholder images with your actual photos")
print("🎨 Customize colors and content as needed")