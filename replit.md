# Overview

This is a monetizable Streamlit-based music artist guessing game focused on Argentine/Latin trap and urban music artists. The application features a Y2K/Pinterest aesthetic design and presents players with artist photos, challenging them to guess which artist has more monthly listeners on streaming platforms. The game now includes 69 artists from the Latin urban music scene, ranging from mainstream acts like "zell" (701K listeners) to emerging artists with smaller followings.

# Recent Changes (August 25, 2025)

## Visual Design Overhaul
- Implemented Y2K/Pinterest aesthetic with gradient backgrounds and modern styling
- Added responsive background image support
- Enhanced card designs with hover effects and backdrop filters
- Improved mobile responsiveness
- Added Instagram link integration (@j040.fr)

## Monetization Features  
- Added designated ad spaces for premium partnerships
- Prepared layout for Google AdSense integration
- Included spaces for artist promotion and collaborations
- Enhanced visual hierarchy to support advertising without disrupting UX

## Data Expansion
- Expanded artist database from 35 to 69 artists
- Added new underground artists with current streaming data
- Maintained data structure for easy future additions

# User Preferences

Preferred communication style: Simple, everyday language.
Design preference: Y2K/Pinterest aesthetic with clean monetization integration.

# System Architecture

## Frontend Framework
The application is built using Streamlit with enhanced CSS styling for modern aesthetic appeal:
- Y2K-inspired color schemes and gradients
- Responsive design for desktop and mobile
- Advanced CSS animations and hover effects
- Fixed positioning for social media links

## Monetization Strategy
The application is prepared for multiple revenue streams:
- **Google AdSense**: Strategic ad placements that don't disrupt gameplay
- **Artist Promotions**: Dedicated spaces for independent artist collaborations
- **Premium Features**: Ready for st-paywall implementation for advanced features
- **Social Media Integration**: Direct Instagram link for audience building

## Data Storage
Artist data expanded to include 69 artists stored in Python dictionary structure:
- Monthly listener count (integer)
- Photo filename (string) with fallback support for images/ directory
- Enhanced formatting utilities for number display

## Visual Design System
- **Color Palette**: Pink to purple gradients (#ff6b9d to #6a4c93)
- **Typography**: Bold, modern fonts with text shadows and gradient fills
- **Layout**: Card-based design with backdrop filters and hover animations
- **Responsive**: Mobile-first approach with breakpoint optimizations

# External Dependencies

## Core Framework
- **Streamlit**: Enhanced with custom CSS for modern web app aesthetics

## Python Standard Library
- **random**: Artist selection and game mechanics

## Media Assets
- Background image support (external URL or local hosting)
- Local artist images with fallback directory support
- Instagram integration for social media presence

The application is designed for easy monetization while maintaining excellent user experience and modern visual appeal.