# ECOSorter
> Promoting eco-friendly habits with an automated garbage can that sorts waste into garbage, recycling, or compost automatically!

### Table of Contents
- [Introduction](https://github.com/abs5467/EcoSorter#introduction)
- [Background](https://github.com/abs5467/EcoSorter#background)
- [Design](https://github.com/abs5467/EcoSorter#design)
- [Impacts](https://github.com/abs5467/EcoSorter#impacts)
- [Future Iterations](https://github.com/abs5467/EcoSorter#future-iterations)
- [Research References](https://github.com/abs5467/EcoSorter#research-references)

## Introduction
I participated in the Metropolitan Engineering Competition at Toronto Metropolitan University (TMU) in the Innovative Design Category by developing EcoSorter, an automated waste-sorting system, in a team of 6 members. The 6 members included students of multiple engineering disciplines, such as computer, electrical, aerospace, and biomedical. We worked together to bring a physical prototype, some technical components, like a code written in Python, and a 20-minute slideshow presentation. Out of 11 teams, our team secured 4th place, showcasing our innovative approach and hard work.

---
## Background
From our research, we see that Toronto produces nearly 830,000 tonnes of waste annually, with a diversion rate of about 48.6%, meaning over half of the city's waste still ends up in landfills. A significant portion of this waste is misplaced, with 77% of materials in large city garbage bins being incorrectly discarded. Most of Toronto's waste is sent to the Green Lane Landfill, which could reach full capacity by 2034-2035. Given this, we decided to design ECOSorter.

Unlike standard trash cans, ECOSorter offers an innovative automated sorting system, making waste disposal more efficient. Compared to other automated trash can models, like Russia's limited public automated trash cans and Pan Am's time-consuming sorting, which also requires human assistance, ECOSorter allows for quick, automated waste disposal for not only the public but for households as well.

---
## Design
#### Physical Design
Our design features a standard trash can divided into three sections, garbage, recycling, and compost. When the waste is thrown into the trash can, it lands on a surface with cameras that take a picture of the waste. The images taken will then be processed through Python code using machine learning to identify the waste. Based on the output given by the code, the system adjusts the platform's planks to guide the waste into the correct bin. 

- Images of the physical prototype and CAD design can be found below.

#### Code Design
I worked on the code for ECOSorter using Python and TensorFlow with machine learning to predict images of waste and determine the correct disposal location. The system identifies the prediction with the highest percentage, and this information is used to automate the sorting and disposal process.

- This code can be accessed through the master branch.

#### Images of the Design
![dimensions](https://github.com/user-attachments/assets/3ed3ce73-f3b1-4a28-ae9e-c24a5939f5d3)
![rotations&angles](https://github.com/user-attachments/assets/41ba48b5-5f2f-4e95-a05b-2893d21ef217)
![joint_mechanisms](https://github.com/user-attachments/assets/c589e3ba-1bb0-4f3e-bb35-52b8072c8469)

---
## Impacts
- **Technical Impacts**:
ECOSoter uses machine learning to ease waste sorting, which helps in reducing landfill waste and minimizing the need for human intervention. However, it may face errors in waste identification and may require regular maintenance.
- **Social Impacts**:
ECOSorter has positive social impacts as it improves health through reduced pollution and fosters a culture of sustainability while addressing the lack of waste sorting education. However, it may reduce the motivation for people to educate themselves on sustainability issues.
- **Environmental Impacts**:
ECOSorter helps reduce landfill waste and environmental harm by lowering greenhouse gas emissions, saving resources through recycling, preventing pollution from hazardous waste, and conserving energy with efficient recycling practices.
- **Economic Impacts**:
ECOSorter reduces waste management and energy costs, generates revenue from recycling and composting, saves raw material expenses, and creates jobs in the waste management sector.

---
## Future Iterations
- **Light Refraction Detection**:
  - This would add the ability to differentiate from materials and improve object recognition.
- **Weight & International Food Detection**:
  - A steel plank can be used to help recognize objects using weight as it can withstand a weight of up to 250 lbs.
  - We can also implement a way of identifying certain foods based on set properties which will help sort various food waste from different cultures.
- **Cleaning Mechanism**:
  - The heat cleaning mechanism used in dishwashers can be implemented to help clean the planks between uses to avoid contamination.
---

## Research References


