# Supraorbital-greateroccipital-nerves

This repository is an extension to an anatomy article that describes the morphology of the supraorbital and greater occipital nerves using 3D registrations and visualization. It includes 3D models of CT-scan skulls with the associated nerves projected on them, as well as source code and documentation related to the generation of these models and calculations of nerve morphology.

## Folder Structure

The repository consists of the following folders:

### 1. 3D-models

This folder contains rendered 3D models of CT-scan skulls and the associated nerves. The models are generated through 3D stylus registrations and are available in multiple mesh types for user convenience. The following mesh types are provided:

- .stl (STereoLithography format)
- .obj (Wavefront OBJ format)
- .x3d (Extensible 3D format)
- .ply (Polygon File Format)

The models are available in both original colors and grayscale, depending on the mesh type chosen.

The models can be viewed directly in the GitHub UI by clicking on the .stl files. GitHub provides a 3D viewer that allows you to interact with the models, zooming in, rotating, and inspecting them from different angles.

For a more comprehensive viewing experience, you can download the 3D models and view them in a software program of your choice. One recommended program is MeshLab, which is a free and open-source software widely used for 3D model visualization and editing. You can download MeshLab from their official website [here](https://www.meshlab.net/).

To view the downloaded models in MeshLab:

1. Open MeshLab and select "File" from the menu.

2. Choose "Import Mesh" and navigate to the location where you downloaded the 3D models.

3. Select the desired mesh file format (.stl, .obj, .x3d, .ply) and open the corresponding file.

4. Once imported, you can explore the 3D model using MeshLab's intuitive interface. Use the navigation controls to zoom, rotate, and pan around the model. Additionally, MeshLab offers various visualization and analysis tools that you can utilize to further investigate the morphology of the supraorbital and greater occipital nerves.

Feel free to experiment with the models and use the provided source code and documentation to gain insights into the morphology of the nerves.

### 2. src

This folder contains the source code and additional files for generating the 3D models and performing calculations related to nerve morphology. It includes the following subfolders:

#### 2.1 Skull-projections

This subfolder contains the source code used to generate the 3D models, as well as an extensive documentation provided in the form of a Jupyter notebook. The Jupyter notebook guides users through the process of generating 3D models from CT scans and landmark data. It includes step-by-step instructions, explanations, and examples to facilitate understanding and reproducibility.

#### 2.2 Calculations

This subfolder contains Python files and data used for calculating the morphology of the nerves and generating simple 3D plots. The files and data are organized to enable users to explore and analyze the characteristics and properties of the supraorbital and greater occipital nerves.

## Contribution

Contributions to this repository are welcome. If you would like to contribute, please follow these steps:

1. Fork the repository to your own GitHub account.

2. Create a new branch and make your changes.

3. Commit your changes and push the branch to your forked repository.

4. Submit a pull request, describing the changes you have made and the purpose of your contribution.

Please ensure that your contributions align with the scope and objectives of this repository.

## License

This repository is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute the code and data, provided you include the appropriate attribution and adhere to the license terms.

## Contact

For any questions, concerns, or suggestions related to this repository, please feel free to contact us at nicolas.van.vlasselaer@vub.be