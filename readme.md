# User Manual

## Quick Start Guide

1. **Initialization**: Turn on the bus stop display unit. Ensure it's receiving power from the solar panel.
2. **Display Activation**: Check that the LED matrix display shows the current time and bus arrival estimates.
3. **Out of Service Protocol**: If a bus is out of service, activate the RED switch to update the display status.

## System Overview

- **Accuracy**: The timer display boasts an accuracy of within ±1 minute under normal operating conditions.
- **Operational Constraints**: The system operates from 0700 to 1930 hours, with automatic power management.
- **Visibility**: Designed for clear visibility up to 8 feet away, even in varied weather conditions like smog and rain.
- **Maintenance**: Requires minimal upkeep.

## Detailed Features

- **Backend Architecture**: Utilizes efficient data storage and timing algorithms to estimate bus arrivals with high precision.
- **Frontend Design**: The user interface is intuitive, providing real-time updates and error notifications (display reads '999' for errors).
- **Feedback System**: Includes a mechanism for user feedback and reporting issues related to bus services.
- **Resilience**: The display unit is built to withstand all weather conditions experienced in Delhi.

## Handling Interruptions

- **Midway Stops**: The system dynamically adjusts the timer to account for unexpected delays, ensuring continued accuracy.
- **Bus Out of Service**: When a bus is marked out of service, the system immediately reflects this change on the display for commuters' convenience.

## Additional Information

- **Centralized Control**: All operations are centrally managed, with detailed logs available for performance review.
- **Emergency Stops**: In case of emergencies, buses follow a predefined protocol to ensure passenger safety.

For a comprehensive understanding of the system, including diagrams and technical specifications, please refer to the full project report.
