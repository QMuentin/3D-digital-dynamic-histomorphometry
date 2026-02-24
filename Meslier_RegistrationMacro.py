"""


:author: 
:contact: 
:email: 
:organization: 
:address: 
:copyright: 
:date: May 14 2025 16:58
:dragonflyVersion: 2024.1.0.1619
:UUID: b5009586310b11f08b905cb26d1a4a9a
"""

__version__ = '1.0.2'

"""


:author: 
:contact: 
:email: 
:organization: 
:address: 
:copyright: 
:date: May 14 2025 16:37
:dragonflyVersion: 2024.1.0.1619
:UUID: b5009586310b11f08b905cb26d1a4a9a
"""

# Action log Wed May 14 16:58:15 2025

# Macro name: QM_Registration_v1

# ********** BEGIN MACRO ********** #
"""
Register a moving dataset with a fixed dataset.

:name: register
:execution: execute

:param fixedChannel: reference dataset (fixed in space).
:type fixedChannel: ORSModel.ors.Channel
:param movingChannel: moving dataset.
:type movingChannel: ORSModel.ors.Channel
:param useScale: if True, the scale factor will be used.
:type useScale: bool
:param useRotation: if True, the rotation factor will be used.
:type useRotation: bool
:param useTranslation: if True, the translation factor will be used.
:type useTranslation: bool
:param xScaleInitial: initial value for the scale factor in the X direction
:type xScaleInitial: float
:param yScaleInitial: initial value for the scale factor in the Y direction
:type yScaleInitial: float
:param zScaleInitial: initial value for the scale factor in the Z direction
:type zScaleInitial: float
:param xRotationInitial: initial value for the rotation factor in the X direction
:type xRotationInitial: float
:param yRotationInitial: initial value for the rotation factor in the Y direction
:type yRotationInitial: float
:param zRotationInitial: initial value for the rotation factor in the Z direction
:type zRotationInitial: float
:param xTranslationInitial: initial value for the translation factor in the X direction
:type xTranslationInitial: float
:param yTranslationInitial: initial value for the translation factor in the Y direction
:type yTranslationInitial: float
:param zTranslationInitial: initial value for the translation factor in the Z direction
:type zTranslationInitial: float
:param xScaleSmallest: final value for the scale factor in the X direction
:type xScaleSmallest: float
:param yScaleSmallest: final value for the scale factor in the Y direction
:type yScaleSmallest: float
:param zScaleSmallest: final value for the scale factor in the Z direction
:type zScaleSmallest: float
:param xRotationSmallest: final value for the rotation factor in the X direction
:type xRotationSmallest: float
:param yRotationSmallest: final value for the rotation factor in the Y direction
:type yRotationSmallest: float
:param zRotationSmallest: final value for the rotation factor in the Z direction
:type zRotationSmallest: float
:param xTranslationSmallest: final value for the translation factor in the X direction
:type xTranslationSmallest: float
:param yTranslationSmallest: final value for the translation factor in the Y direction
:type yTranslationSmallest: float
:param zTranslationSmallest: final value for the translation factor in the Z direction
:type zTranslationSmallest: float
:param nearestInterpolationMethod: if True, the nearest interpolation method will be used; if False, the linear interpolation will be used.
:type nearestInterpolationMethod: bool
:param mutualInfoRegistrationMethod: if True, the mutual information registration algorithm will be used; if False, the SSD registration algorithm will be used.
:type mutualInfoRegistrationMethod: bool
:param xSampling: sampling in the X direction for the similarity metric
:type xSampling: int
:param ySampling: sampling in the Y direction for the similarity metric
:type ySampling: int
:param zSampling: sampling in the Z direction for the similarity metric
:type zSampling: int
:param mask: Visual Shape 3D or ROI that mask pixels of fixed dataset to make a scored registration.
:type mask: ORSModel.ors.ROI, ORSModel.ors.VisualShape3D
:param useMultiScale: Use a multiscale step in the registration
:type useMultiScale: bool

:return transformationMatrix: transformation matrix to go from the original location of the moving dataset to the final location of the moving dataset
:rtype transformationMatrix: ORSModel.ors.Matrix4x4
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
useScale = False

useRotation = True

useTranslation = True

xScaleInitial = 0.1

yScaleInitial = 0.1

zScaleInitial = 0.1

xRotationInitial = 0.17453292519943295

yRotationInitial = 0.17453292519943295

zRotationInitial = 0.17453292519943295

xTranslationInitial = 0.00015

yTranslationInitial = 0.00015

zTranslationInitial = 0.00015

xScaleSmallest = 0.001

yScaleSmallest = 0.001

zScaleSmallest = 0.001

xRotationSmallest = 0.008726646259971648

yRotationSmallest = 0.008726646259971648

zRotationSmallest = 0.008726646259971648

xTranslationSmallest = 1.1e-05

yTranslationSmallest = 1.1e-05

zTranslationSmallest = 1.1e-05

nearestInterpolationMethod = False

mutualInfoRegistrationMethod = True

xSampling = 1

ySampling = 1

zSampling = 1

mask = None

useMultiScale = True

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
transformationMatrix = OrsRigidRegistrationModel.register(fixedChannel=fixedChannel,
                                                          movingChannel=movingChannel,
                                                          useScale=useScale,
                                                          useRotation=useRotation,
                                                          useTranslation=useTranslation,
                                                          xScaleInitial=xScaleInitial,
                                                          yScaleInitial=yScaleInitial,
                                                          zScaleInitial=zScaleInitial,
                                                          xRotationInitial=xRotationInitial,
                                                          yRotationInitial=yRotationInitial,
                                                          zRotationInitial=zRotationInitial,
                                                          xTranslationInitial=xTranslationInitial,
                                                          yTranslationInitial=yTranslationInitial,
                                                          zTranslationInitial=zTranslationInitial,
                                                          xScaleSmallest=xScaleSmallest,
                                                          yScaleSmallest=yScaleSmallest,
                                                          zScaleSmallest=zScaleSmallest,
                                                          xRotationSmallest=xRotationSmallest,
                                                          yRotationSmallest=yRotationSmallest,
                                                          zRotationSmallest=zRotationSmallest,
                                                          xTranslationSmallest=xTranslationSmallest,
                                                          yTranslationSmallest=yTranslationSmallest,
                                                          zTranslationSmallest=zTranslationSmallest,
                                                          nearestInterpolationMethod=nearestInterpolationMethod,
                                                          mutualInfoRegistrationMethod=mutualInfoRegistrationMethod,
                                                          xSampling=xSampling,
                                                          ySampling=ySampling,
                                                          zSampling=zSampling,
                                                          mask=mask,
                                                          useMultiScale=useMultiScale)

# ----- BEGIN RETURNED VALUES DEFINITION ----- #
# transformationMatrix = orsMatrix(0.9884380236004251, -0.15160382388601087, 0.002560094534305063, 0.0014301584092981691, 0.15054169582314209, 0.9792181618315664, -0.13590065988765843, 0.0063674856013252014, 0.018096168643603996, 0.13471478063801248, 0.99071916129550774, -0.00094611490840511986, 0, 0, 0, 1)

# ----- END RETURNED VALUES DEFINITION ----- #
# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Register a moving dataset with a fixed dataset.

:name: register
:execution: execute

:param fixedChannel: reference dataset (fixed in space).
:type fixedChannel: ORSModel.ors.Channel
:param movingChannel: moving dataset.
:type movingChannel: ORSModel.ors.Channel
:param useScale_2: if True, the scale factor will be used.
:type useScale_2: bool
:param useRotation_2: if True, the rotation factor will be used.
:type useRotation_2: bool
:param useTranslation_2: if True, the translation factor will be used.
:type useTranslation_2: bool
:param xScaleInitial_2: initial value for the scale factor in the X direction
:type xScaleInitial_2: float
:param yScaleInitial_2: initial value for the scale factor in the Y direction
:type yScaleInitial_2: float
:param zScaleInitial_2: initial value for the scale factor in the Z direction
:type zScaleInitial_2: float
:param xRotationInitial_2: initial value for the rotation factor in the X direction
:type xRotationInitial_2: float
:param yRotationInitial_2: initial value for the rotation factor in the Y direction
:type yRotationInitial_2: float
:param zRotationInitial_2: initial value for the rotation factor in the Z direction
:type zRotationInitial_2: float
:param xTranslationInitial_2: initial value for the translation factor in the X direction
:type xTranslationInitial_2: float
:param yTranslationInitial_2: initial value for the translation factor in the Y direction
:type yTranslationInitial_2: float
:param zTranslationInitial_2: initial value for the translation factor in the Z direction
:type zTranslationInitial_2: float
:param xScaleSmallest_2: final value for the scale factor in the X direction
:type xScaleSmallest_2: float
:param yScaleSmallest_2: final value for the scale factor in the Y direction
:type yScaleSmallest_2: float
:param zScaleSmallest_2: final value for the scale factor in the Z direction
:type zScaleSmallest_2: float
:param xRotationSmallest_2: final value for the rotation factor in the X direction
:type xRotationSmallest_2: float
:param yRotationSmallest_2: final value for the rotation factor in the Y direction
:type yRotationSmallest_2: float
:param zRotationSmallest_2: final value for the rotation factor in the Z direction
:type zRotationSmallest_2: float
:param xTranslationSmallest_2: final value for the translation factor in the X direction
:type xTranslationSmallest_2: float
:param yTranslationSmallest_2: final value for the translation factor in the Y direction
:type yTranslationSmallest_2: float
:param zTranslationSmallest_2: final value for the translation factor in the Z direction
:type zTranslationSmallest_2: float
:param nearestInterpolationMethod_2: if True, the nearest interpolation method will be used; if False, the linear interpolation will be used.
:type nearestInterpolationMethod_2: bool
:param mutualInfoRegistrationMethod_2: if True, the mutual information registration algorithm will be used; if False, the SSD registration algorithm will be used.
:type mutualInfoRegistrationMethod_2: bool
:param xSampling_2: sampling in the X direction for the similarity metric
:type xSampling_2: int
:param ySampling_2: sampling in the Y direction for the similarity metric
:type ySampling_2: int
:param zSampling_2: sampling in the Z direction for the similarity metric
:type zSampling_2: int
:param mask_2: Visual Shape 3D or ROI that mask pixels of fixed dataset to make a scored registration.
:type mask_2: ORSModel.ors.ROI, ORSModel.ors.VisualShape3D
:param useMultiScale_2: Use a multiscale step in the registration
:type useMultiScale_2: bool

:return transformationMatrix_2: transformation matrix to go from the original location of the moving dataset to the final location of the moving dataset
:rtype transformationMatrix_2: ORSModel.ors.Matrix4x4
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
useScale_2 = False

useRotation_2 = True

useTranslation_2 = True

xScaleInitial_2 = 0.1

yScaleInitial_2 = 0.1

zScaleInitial_2 = 0.1

xRotationInitial_2 = 0.17453292519943295

yRotationInitial_2 = 0.17453292519943295

zRotationInitial_2 = 0.17453292519943295

xTranslationInitial_2 = 0.00015

yTranslationInitial_2 = 0.00015

zTranslationInitial_2 = 0.00015

xScaleSmallest_2 = 0.001

yScaleSmallest_2 = 0.001

zScaleSmallest_2 = 0.001

xRotationSmallest_2 = 0.008726646259971648

yRotationSmallest_2 = 0.008726646259971648

zRotationSmallest_2 = 0.008726646259971648

xTranslationSmallest_2 = 1.1e-05

yTranslationSmallest_2 = 1.1e-05

zTranslationSmallest_2 = 1.1e-05

nearestInterpolationMethod_2 = False

mutualInfoRegistrationMethod_2 = True

xSampling_2 = 1

ySampling_2 = 1

zSampling_2 = 1

mask_2 = None

useMultiScale_2 = True

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
transformationMatrix_2 = OrsRigidRegistrationModel.register(fixedChannel=fixedChannel,
                                                            movingChannel=movingChannel,
                                                            useScale=useScale_2,
                                                            useRotation=useRotation_2,
                                                            useTranslation=useTranslation_2,
                                                            xScaleInitial=xScaleInitial_2,
                                                            yScaleInitial=yScaleInitial_2,
                                                            zScaleInitial=zScaleInitial_2,
                                                            xRotationInitial=xRotationInitial_2,
                                                            yRotationInitial=yRotationInitial_2,
                                                            zRotationInitial=zRotationInitial_2,
                                                            xTranslationInitial=xTranslationInitial_2,
                                                            yTranslationInitial=yTranslationInitial_2,
                                                            zTranslationInitial=zTranslationInitial_2,
                                                            xScaleSmallest=xScaleSmallest_2,
                                                            yScaleSmallest=yScaleSmallest_2,
                                                            zScaleSmallest=zScaleSmallest_2,
                                                            xRotationSmallest=xRotationSmallest_2,
                                                            yRotationSmallest=yRotationSmallest_2,
                                                            zRotationSmallest=zRotationSmallest_2,
                                                            xTranslationSmallest=xTranslationSmallest_2,
                                                            yTranslationSmallest=yTranslationSmallest_2,
                                                            zTranslationSmallest=zTranslationSmallest_2,
                                                            nearestInterpolationMethod=nearestInterpolationMethod_2,
                                                            mutualInfoRegistrationMethod=mutualInfoRegistrationMethod_2,
                                                            xSampling=xSampling_2,
                                                            ySampling=ySampling_2,
                                                            zSampling=zSampling_2,
                                                            mask=mask_2,
                                                            useMultiScale=useMultiScale_2)

# ----- BEGIN RETURNED VALUES DEFINITION ----- #
# transformationMatrix_2 = orsMatrix(1, 1.5341460740669888e-17, 0, 0, -1.1275702593849246e-17, 1, 0, 3.4694469519536142e-18, 8.6736173798840355e-19, 2.7755575615628914e-17, 1, -6.9388939039072284e-18, 0, 0, 0, 1)

# ----- END RETURNED VALUES DEFINITION ----- #
# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Register a moving dataset with a fixed dataset.

:name: register
:execution: execute

:param fixedChannel: reference dataset (fixed in space).
:type fixedChannel: ORSModel.ors.Channel
:param movingChannel: moving dataset.
:type movingChannel: ORSModel.ors.Channel
:param useScale_3: if True, the scale factor will be used.
:type useScale_3: bool
:param useRotation_3: if True, the rotation factor will be used.
:type useRotation_3: bool
:param useTranslation_3: if True, the translation factor will be used.
:type useTranslation_3: bool
:param xScaleInitial_3: initial value for the scale factor in the X direction
:type xScaleInitial_3: float
:param yScaleInitial_3: initial value for the scale factor in the Y direction
:type yScaleInitial_3: float
:param zScaleInitial_3: initial value for the scale factor in the Z direction
:type zScaleInitial_3: float
:param xRotationInitial_3: initial value for the rotation factor in the X direction
:type xRotationInitial_3: float
:param yRotationInitial_3: initial value for the rotation factor in the Y direction
:type yRotationInitial_3: float
:param zRotationInitial_3: initial value for the rotation factor in the Z direction
:type zRotationInitial_3: float
:param xTranslationInitial_3: initial value for the translation factor in the X direction
:type xTranslationInitial_3: float
:param yTranslationInitial_3: initial value for the translation factor in the Y direction
:type yTranslationInitial_3: float
:param zTranslationInitial_3: initial value for the translation factor in the Z direction
:type zTranslationInitial_3: float
:param xScaleSmallest_3: final value for the scale factor in the X direction
:type xScaleSmallest_3: float
:param yScaleSmallest_3: final value for the scale factor in the Y direction
:type yScaleSmallest_3: float
:param zScaleSmallest_3: final value for the scale factor in the Z direction
:type zScaleSmallest_3: float
:param xRotationSmallest_3: final value for the rotation factor in the X direction
:type xRotationSmallest_3: float
:param yRotationSmallest_3: final value for the rotation factor in the Y direction
:type yRotationSmallest_3: float
:param zRotationSmallest_3: final value for the rotation factor in the Z direction
:type zRotationSmallest_3: float
:param xTranslationSmallest_3: final value for the translation factor in the X direction
:type xTranslationSmallest_3: float
:param yTranslationSmallest_3: final value for the translation factor in the Y direction
:type yTranslationSmallest_3: float
:param zTranslationSmallest_3: final value for the translation factor in the Z direction
:type zTranslationSmallest_3: float
:param nearestInterpolationMethod_3: if True, the nearest interpolation method will be used; if False, the linear interpolation will be used.
:type nearestInterpolationMethod_3: bool
:param mutualInfoRegistrationMethod_3: if True, the mutual information registration algorithm will be used; if False, the SSD registration algorithm will be used.
:type mutualInfoRegistrationMethod_3: bool
:param xSampling_3: sampling in the X direction for the similarity metric
:type xSampling_3: int
:param ySampling_3: sampling in the Y direction for the similarity metric
:type ySampling_3: int
:param zSampling_3: sampling in the Z direction for the similarity metric
:type zSampling_3: int
:param mask_3: Visual Shape 3D or ROI that mask pixels of fixed dataset to make a scored registration.
:type mask_3: ORSModel.ors.ROI, ORSModel.ors.VisualShape3D
:param useMultiScale_3: Use a multiscale step in the registration
:type useMultiScale_3: bool

:return transformationMatrix_3: transformation matrix to go from the original location of the moving dataset to the final location of the moving dataset
:rtype transformationMatrix_3: ORSModel.ors.Matrix4x4
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
useScale_3 = False

useRotation_3 = True

useTranslation_3 = True

xScaleInitial_3 = 0.1

yScaleInitial_3 = 0.1

zScaleInitial_3 = 0.1

xRotationInitial_3 = 0.17453292519943295

yRotationInitial_3 = 0.17453292519943295

zRotationInitial_3 = 0.17453292519943295

xTranslationInitial_3 = 0.00015

yTranslationInitial_3 = 0.00015

zTranslationInitial_3 = 0.00015

xScaleSmallest_3 = 0.001

yScaleSmallest_3 = 0.001

zScaleSmallest_3 = 0.001

xRotationSmallest_3 = 0.008726646259971648

yRotationSmallest_3 = 0.008726646259971648

zRotationSmallest_3 = 0.008726646259971648

xTranslationSmallest_3 = 1.1e-05

yTranslationSmallest_3 = 1.1e-05

zTranslationSmallest_3 = 1.1e-05

nearestInterpolationMethod_3 = False

mutualInfoRegistrationMethod_3 = True

xSampling_3 = 1

ySampling_3 = 1

zSampling_3 = 1

mask_3 = None

useMultiScale_3 = True

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
transformationMatrix_3 = OrsRigidRegistrationModel.register(fixedChannel=fixedChannel,
                                                            movingChannel=movingChannel,
                                                            useScale=useScale_3,
                                                            useRotation=useRotation_3,
                                                            useTranslation=useTranslation_3,
                                                            xScaleInitial=xScaleInitial_3,
                                                            yScaleInitial=yScaleInitial_3,
                                                            zScaleInitial=zScaleInitial_3,
                                                            xRotationInitial=xRotationInitial_3,
                                                            yRotationInitial=yRotationInitial_3,
                                                            zRotationInitial=zRotationInitial_3,
                                                            xTranslationInitial=xTranslationInitial_3,
                                                            yTranslationInitial=yTranslationInitial_3,
                                                            zTranslationInitial=zTranslationInitial_3,
                                                            xScaleSmallest=xScaleSmallest_3,
                                                            yScaleSmallest=yScaleSmallest_3,
                                                            zScaleSmallest=zScaleSmallest_3,
                                                            xRotationSmallest=xRotationSmallest_3,
                                                            yRotationSmallest=yRotationSmallest_3,
                                                            zRotationSmallest=zRotationSmallest_3,
                                                            xTranslationSmallest=xTranslationSmallest_3,
                                                            yTranslationSmallest=yTranslationSmallest_3,
                                                            zTranslationSmallest=zTranslationSmallest_3,
                                                            nearestInterpolationMethod=nearestInterpolationMethod_3,
                                                            mutualInfoRegistrationMethod=mutualInfoRegistrationMethod_3,
                                                            xSampling=xSampling_3,
                                                            ySampling=ySampling_3,
                                                            zSampling=zSampling_3,
                                                            mask=mask_3,
                                                            useMultiScale=useMultiScale_3)

# ----- BEGIN RETURNED VALUES DEFINITION ----- #
# transformationMatrix_3 = orsMatrix(1, 1.5341460740669888e-17, 0, 0, -1.1275702593849246e-17, 1, 0, 3.4694469519536142e-18, 8.6736173798840355e-19, 2.7755575615628914e-17, 1, -6.9388939039072284e-18, 0, 0, 0, 1)

# ----- END RETURNED VALUES DEFINITION ----- #
# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Register a moving dataset with a fixed dataset.

:name: register
:execution: execute

:param fixedChannel: reference dataset (fixed in space).
:type fixedChannel: ORSModel.ors.Channel
:param movingChannel: moving dataset.
:type movingChannel: ORSModel.ors.Channel
:param useScale_4: if True, the scale factor will be used.
:type useScale_4: bool
:param useRotation_4: if True, the rotation factor will be used.
:type useRotation_4: bool
:param useTranslation_4: if True, the translation factor will be used.
:type useTranslation_4: bool
:param xScaleInitial_4: initial value for the scale factor in the X direction
:type xScaleInitial_4: float
:param yScaleInitial_4: initial value for the scale factor in the Y direction
:type yScaleInitial_4: float
:param zScaleInitial_4: initial value for the scale factor in the Z direction
:type zScaleInitial_4: float
:param xRotationInitial_4: initial value for the rotation factor in the X direction
:type xRotationInitial_4: float
:param yRotationInitial_4: initial value for the rotation factor in the Y direction
:type yRotationInitial_4: float
:param zRotationInitial_4: initial value for the rotation factor in the Z direction
:type zRotationInitial_4: float
:param xTranslationInitial_4: initial value for the translation factor in the X direction
:type xTranslationInitial_4: float
:param yTranslationInitial_4: initial value for the translation factor in the Y direction
:type yTranslationInitial_4: float
:param zTranslationInitial_4: initial value for the translation factor in the Z direction
:type zTranslationInitial_4: float
:param xScaleSmallest_4: final value for the scale factor in the X direction
:type xScaleSmallest_4: float
:param yScaleSmallest_4: final value for the scale factor in the Y direction
:type yScaleSmallest_4: float
:param zScaleSmallest_4: final value for the scale factor in the Z direction
:type zScaleSmallest_4: float
:param xRotationSmallest_4: final value for the rotation factor in the X direction
:type xRotationSmallest_4: float
:param yRotationSmallest_4: final value for the rotation factor in the Y direction
:type yRotationSmallest_4: float
:param zRotationSmallest_4: final value for the rotation factor in the Z direction
:type zRotationSmallest_4: float
:param xTranslationSmallest_4: final value for the translation factor in the X direction
:type xTranslationSmallest_4: float
:param yTranslationSmallest_4: final value for the translation factor in the Y direction
:type yTranslationSmallest_4: float
:param zTranslationSmallest_4: final value for the translation factor in the Z direction
:type zTranslationSmallest_4: float
:param nearestInterpolationMethod_4: if True, the nearest interpolation method will be used; if False, the linear interpolation will be used.
:type nearestInterpolationMethod_4: bool
:param mutualInfoRegistrationMethod_4: if True, the mutual information registration algorithm will be used; if False, the SSD registration algorithm will be used.
:type mutualInfoRegistrationMethod_4: bool
:param xSampling_4: sampling in the X direction for the similarity metric
:type xSampling_4: int
:param ySampling_4: sampling in the Y direction for the similarity metric
:type ySampling_4: int
:param zSampling_4: sampling in the Z direction for the similarity metric
:type zSampling_4: int
:param mask_4: Visual Shape 3D or ROI that mask pixels of fixed dataset to make a scored registration.
:type mask_4: ORSModel.ors.ROI, ORSModel.ors.VisualShape3D
:param useMultiScale_4: Use a multiscale step in the registration
:type useMultiScale_4: bool

:return transformationMatrix_4: transformation matrix to go from the original location of the moving dataset to the final location of the moving dataset
:rtype transformationMatrix_4: ORSModel.ors.Matrix4x4
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
useScale_4 = False

useRotation_4 = True

useTranslation_4 = True

xScaleInitial_4 = 0.1

yScaleInitial_4 = 0.1

zScaleInitial_4 = 0.1

xRotationInitial_4 = 0.17453292519943295

yRotationInitial_4 = 0.17453292519943295

zRotationInitial_4 = 0.17453292519943295

xTranslationInitial_4 = 0.00015

yTranslationInitial_4 = 0.00015

zTranslationInitial_4 = 0.00015

xScaleSmallest_4 = 0.001

yScaleSmallest_4 = 0.001

zScaleSmallest_4 = 0.001

xRotationSmallest_4 = 0.008726646259971648

yRotationSmallest_4 = 0.008726646259971648

zRotationSmallest_4 = 0.008726646259971648

xTranslationSmallest_4 = 1.1e-05

yTranslationSmallest_4 = 1.1e-05

zTranslationSmallest_4 = 1.1e-05

nearestInterpolationMethod_4 = False

mutualInfoRegistrationMethod_4 = True

xSampling_4 = 1

ySampling_4 = 1

zSampling_4 = 1

mask_4 = None

useMultiScale_4 = True

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
transformationMatrix_4 = OrsRigidRegistrationModel.register(fixedChannel=fixedChannel,
                                                            movingChannel=movingChannel,
                                                            useScale=useScale_4,
                                                            useRotation=useRotation_4,
                                                            useTranslation=useTranslation_4,
                                                            xScaleInitial=xScaleInitial_4,
                                                            yScaleInitial=yScaleInitial_4,
                                                            zScaleInitial=zScaleInitial_4,
                                                            xRotationInitial=xRotationInitial_4,
                                                            yRotationInitial=yRotationInitial_4,
                                                            zRotationInitial=zRotationInitial_4,
                                                            xTranslationInitial=xTranslationInitial_4,
                                                            yTranslationInitial=yTranslationInitial_4,
                                                            zTranslationInitial=zTranslationInitial_4,
                                                            xScaleSmallest=xScaleSmallest_4,
                                                            yScaleSmallest=yScaleSmallest_4,
                                                            zScaleSmallest=zScaleSmallest_4,
                                                            xRotationSmallest=xRotationSmallest_4,
                                                            yRotationSmallest=yRotationSmallest_4,
                                                            zRotationSmallest=zRotationSmallest_4,
                                                            xTranslationSmallest=xTranslationSmallest_4,
                                                            yTranslationSmallest=yTranslationSmallest_4,
                                                            zTranslationSmallest=zTranslationSmallest_4,
                                                            nearestInterpolationMethod=nearestInterpolationMethod_4,
                                                            mutualInfoRegistrationMethod=mutualInfoRegistrationMethod_4,
                                                            xSampling=xSampling_4,
                                                            ySampling=ySampling_4,
                                                            zSampling=zSampling_4,
                                                            mask=mask_4,
                                                            useMultiScale=useMultiScale_4)

# ----- BEGIN RETURNED VALUES DEFINITION ----- #
# transformationMatrix_4 = orsMatrix(1, 1.5341460740669888e-17, 0, 0, -1.1275702593849246e-17, 1, 0, 3.4694469519536142e-18, 8.6736173798840355e-19, 2.7755575615628914e-17, 1, -6.9388939039072284e-18, 0, 0, 0, 1)

# ----- END RETURNED VALUES DEFINITION ----- #
# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Register a moving dataset with a fixed dataset.

:name: register
:execution: execute

:param fixedChannel: reference dataset (fixed in space).
:type fixedChannel: ORSModel.ors.Channel
:param movingChannel: moving dataset.
:type movingChannel: ORSModel.ors.Channel
:param useScale_5: if True, the scale factor will be used.
:type useScale_5: bool
:param useRotation_5: if True, the rotation factor will be used.
:type useRotation_5: bool
:param useTranslation_5: if True, the translation factor will be used.
:type useTranslation_5: bool
:param xScaleInitial_5: initial value for the scale factor in the X direction
:type xScaleInitial_5: float
:param yScaleInitial_5: initial value for the scale factor in the Y direction
:type yScaleInitial_5: float
:param zScaleInitial_5: initial value for the scale factor in the Z direction
:type zScaleInitial_5: float
:param xRotationInitial_5: initial value for the rotation factor in the X direction
:type xRotationInitial_5: float
:param yRotationInitial_5: initial value for the rotation factor in the Y direction
:type yRotationInitial_5: float
:param zRotationInitial_5: initial value for the rotation factor in the Z direction
:type zRotationInitial_5: float
:param xTranslationInitial_5: initial value for the translation factor in the X direction
:type xTranslationInitial_5: float
:param yTranslationInitial_5: initial value for the translation factor in the Y direction
:type yTranslationInitial_5: float
:param zTranslationInitial_5: initial value for the translation factor in the Z direction
:type zTranslationInitial_5: float
:param xScaleSmallest_5: final value for the scale factor in the X direction
:type xScaleSmallest_5: float
:param yScaleSmallest_5: final value for the scale factor in the Y direction
:type yScaleSmallest_5: float
:param zScaleSmallest_5: final value for the scale factor in the Z direction
:type zScaleSmallest_5: float
:param xRotationSmallest_5: final value for the rotation factor in the X direction
:type xRotationSmallest_5: float
:param yRotationSmallest_5: final value for the rotation factor in the Y direction
:type yRotationSmallest_5: float
:param zRotationSmallest_5: final value for the rotation factor in the Z direction
:type zRotationSmallest_5: float
:param xTranslationSmallest_5: final value for the translation factor in the X direction
:type xTranslationSmallest_5: float
:param yTranslationSmallest_5: final value for the translation factor in the Y direction
:type yTranslationSmallest_5: float
:param zTranslationSmallest_5: final value for the translation factor in the Z direction
:type zTranslationSmallest_5: float
:param nearestInterpolationMethod_5: if True, the nearest interpolation method will be used; if False, the linear interpolation will be used.
:type nearestInterpolationMethod_5: bool
:param mutualInfoRegistrationMethod_5: if True, the mutual information registration algorithm will be used; if False, the SSD registration algorithm will be used.
:type mutualInfoRegistrationMethod_5: bool
:param xSampling_5: sampling in the X direction for the similarity metric
:type xSampling_5: int
:param ySampling_5: sampling in the Y direction for the similarity metric
:type ySampling_5: int
:param zSampling_5: sampling in the Z direction for the similarity metric
:type zSampling_5: int
:param mask_5: Visual Shape 3D or ROI that mask pixels of fixed dataset to make a scored registration.
:type mask_5: ORSModel.ors.ROI, ORSModel.ors.VisualShape3D
:param useMultiScale_5: Use a multiscale step in the registration
:type useMultiScale_5: bool

:return transformationMatrix_5: transformation matrix to go from the original location of the moving dataset to the final location of the moving dataset
:rtype transformationMatrix_5: ORSModel.ors.Matrix4x4
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
useScale_5 = False

useRotation_5 = True

useTranslation_5 = True

xScaleInitial_5 = 0.1

yScaleInitial_5 = 0.1

zScaleInitial_5 = 0.1

xRotationInitial_5 = 0.08726646259971647

yRotationInitial_5 = 0.08726646259971647

zRotationInitial_5 = 0.08726646259971647

xTranslationInitial_5 = 0.0001

yTranslationInitial_5 = 0.0001

zTranslationInitial_5 = 0.0001

xScaleSmallest_5 = 0.001

yScaleSmallest_5 = 0.001

zScaleSmallest_5 = 0.001

xRotationSmallest_5 = 0.00017453292519943296

yRotationSmallest_5 = 0.00017453292519943296

zRotationSmallest_5 = 0.00017453292519943296

xTranslationSmallest_5 = 1e-05

yTranslationSmallest_5 = 1e-05

zTranslationSmallest_5 = 1e-05

nearestInterpolationMethod_5 = False

mutualInfoRegistrationMethod_5 = True

xSampling_5 = 1

ySampling_5 = 1

zSampling_5 = 1

mask_5 = None

useMultiScale_5 = True

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
transformationMatrix_5 = OrsRigidRegistrationModel.register(fixedChannel=fixedChannel,
                                                            movingChannel=movingChannel,
                                                            useScale=useScale_5,
                                                            useRotation=useRotation_5,
                                                            useTranslation=useTranslation_5,
                                                            xScaleInitial=xScaleInitial_5,
                                                            yScaleInitial=yScaleInitial_5,
                                                            zScaleInitial=zScaleInitial_5,
                                                            xRotationInitial=xRotationInitial_5,
                                                            yRotationInitial=yRotationInitial_5,
                                                            zRotationInitial=zRotationInitial_5,
                                                            xTranslationInitial=xTranslationInitial_5,
                                                            yTranslationInitial=yTranslationInitial_5,
                                                            zTranslationInitial=zTranslationInitial_5,
                                                            xScaleSmallest=xScaleSmallest_5,
                                                            yScaleSmallest=yScaleSmallest_5,
                                                            zScaleSmallest=zScaleSmallest_5,
                                                            xRotationSmallest=xRotationSmallest_5,
                                                            yRotationSmallest=yRotationSmallest_5,
                                                            zRotationSmallest=zRotationSmallest_5,
                                                            xTranslationSmallest=xTranslationSmallest_5,
                                                            yTranslationSmallest=yTranslationSmallest_5,
                                                            zTranslationSmallest=zTranslationSmallest_5,
                                                            nearestInterpolationMethod=nearestInterpolationMethod_5,
                                                            mutualInfoRegistrationMethod=mutualInfoRegistrationMethod_5,
                                                            xSampling=xSampling_5,
                                                            ySampling=ySampling_5,
                                                            zSampling=zSampling_5,
                                                            mask=mask_5,
                                                            useMultiScale=useMultiScale_5)

# ----- BEGIN RETURNED VALUES DEFINITION ----- #
# transformationMatrix_5 = orsMatrix(0.99999896924465537, 0.0012879372640734656, 0.00063460793393862406, -4.7577285106676151e-05, -0.0012882024298347572, 0.99999908306759433, 0.00041761042852042629, -1.1352576299958339e-05, -0.0006340694960132922, -0.00041842750154882924, 0.99999971143710853, 9.8494882460331556e-06, 0, 0, 0, 1)

# ----- END RETURNED VALUES DEFINITION ----- #
# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Register a moving dataset with a fixed dataset.

:name: register
:execution: execute

:param fixedChannel: reference dataset (fixed in space).
:type fixedChannel: ORSModel.ors.Channel
:param movingChannel: moving dataset.
:type movingChannel: ORSModel.ors.Channel
:param useScale_6: if True, the scale factor will be used.
:type useScale_6: bool
:param useRotation_6: if True, the rotation factor will be used.
:type useRotation_6: bool
:param useTranslation_6: if True, the translation factor will be used.
:type useTranslation_6: bool
:param xScaleInitial_6: initial value for the scale factor in the X direction
:type xScaleInitial_6: float
:param yScaleInitial_6: initial value for the scale factor in the Y direction
:type yScaleInitial_6: float
:param zScaleInitial_6: initial value for the scale factor in the Z direction
:type zScaleInitial_6: float
:param xRotationInitial_6: initial value for the rotation factor in the X direction
:type xRotationInitial_6: float
:param yRotationInitial_6: initial value for the rotation factor in the Y direction
:type yRotationInitial_6: float
:param zRotationInitial_6: initial value for the rotation factor in the Z direction
:type zRotationInitial_6: float
:param xTranslationInitial_6: initial value for the translation factor in the X direction
:type xTranslationInitial_6: float
:param yTranslationInitial_6: initial value for the translation factor in the Y direction
:type yTranslationInitial_6: float
:param zTranslationInitial_6: initial value for the translation factor in the Z direction
:type zTranslationInitial_6: float
:param xScaleSmallest_6: final value for the scale factor in the X direction
:type xScaleSmallest_6: float
:param yScaleSmallest_6: final value for the scale factor in the Y direction
:type yScaleSmallest_6: float
:param zScaleSmallest_6: final value for the scale factor in the Z direction
:type zScaleSmallest_6: float
:param xRotationSmallest_6: final value for the rotation factor in the X direction
:type xRotationSmallest_6: float
:param yRotationSmallest_6: final value for the rotation factor in the Y direction
:type yRotationSmallest_6: float
:param zRotationSmallest_6: final value for the rotation factor in the Z direction
:type zRotationSmallest_6: float
:param xTranslationSmallest_6: final value for the translation factor in the X direction
:type xTranslationSmallest_6: float
:param yTranslationSmallest_6: final value for the translation factor in the Y direction
:type yTranslationSmallest_6: float
:param zTranslationSmallest_6: final value for the translation factor in the Z direction
:type zTranslationSmallest_6: float
:param nearestInterpolationMethod_6: if True, the nearest interpolation method will be used; if False, the linear interpolation will be used.
:type nearestInterpolationMethod_6: bool
:param mutualInfoRegistrationMethod_6: if True, the mutual information registration algorithm will be used; if False, the SSD registration algorithm will be used.
:type mutualInfoRegistrationMethod_6: bool
:param xSampling_6: sampling in the X direction for the similarity metric
:type xSampling_6: int
:param ySampling_6: sampling in the Y direction for the similarity metric
:type ySampling_6: int
:param zSampling_6: sampling in the Z direction for the similarity metric
:type zSampling_6: int
:param mask_6: Visual Shape 3D or ROI that mask pixels of fixed dataset to make a scored registration.
:type mask_6: ORSModel.ors.ROI, ORSModel.ors.VisualShape3D
:param useMultiScale_6: Use a multiscale step in the registration
:type useMultiScale_6: bool

:return transformationMatrix_6: transformation matrix to go from the original location of the moving dataset to the final location of the moving dataset
:rtype transformationMatrix_6: ORSModel.ors.Matrix4x4
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
useScale_6 = False

useRotation_6 = True

useTranslation_6 = True

xScaleInitial_6 = 0.1

yScaleInitial_6 = 0.1

zScaleInitial_6 = 0.1

xRotationInitial_6 = 0.08726646259971647

yRotationInitial_6 = 0.08726646259971647

zRotationInitial_6 = 0.08726646259971647

xTranslationInitial_6 = 0.0001

yTranslationInitial_6 = 0.0001

zTranslationInitial_6 = 0.0001

xScaleSmallest_6 = 0.001

yScaleSmallest_6 = 0.001

zScaleSmallest_6 = 0.001

xRotationSmallest_6 = 0.00017453292519943296

yRotationSmallest_6 = 0.00017453292519943296

zRotationSmallest_6 = 0.00017453292519943296

xTranslationSmallest_6 = 1e-05

yTranslationSmallest_6 = 1e-05

zTranslationSmallest_6 = 1e-05

nearestInterpolationMethod_6 = False

mutualInfoRegistrationMethod_6 = True

xSampling_6 = 1

ySampling_6 = 1

zSampling_6 = 1

mask_6 = None

useMultiScale_6 = True

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
transformationMatrix_6 = OrsRigidRegistrationModel.register(fixedChannel=fixedChannel,
                                                            movingChannel=movingChannel,
                                                            useScale=useScale_6,
                                                            useRotation=useRotation_6,
                                                            useTranslation=useTranslation_6,
                                                            xScaleInitial=xScaleInitial_6,
                                                            yScaleInitial=yScaleInitial_6,
                                                            zScaleInitial=zScaleInitial_6,
                                                            xRotationInitial=xRotationInitial_6,
                                                            yRotationInitial=yRotationInitial_6,
                                                            zRotationInitial=zRotationInitial_6,
                                                            xTranslationInitial=xTranslationInitial_6,
                                                            yTranslationInitial=yTranslationInitial_6,
                                                            zTranslationInitial=zTranslationInitial_6,
                                                            xScaleSmallest=xScaleSmallest_6,
                                                            yScaleSmallest=yScaleSmallest_6,
                                                            zScaleSmallest=zScaleSmallest_6,
                                                            xRotationSmallest=xRotationSmallest_6,
                                                            yRotationSmallest=yRotationSmallest_6,
                                                            zRotationSmallest=zRotationSmallest_6,
                                                            xTranslationSmallest=xTranslationSmallest_6,
                                                            yTranslationSmallest=yTranslationSmallest_6,
                                                            zTranslationSmallest=zTranslationSmallest_6,
                                                            nearestInterpolationMethod=nearestInterpolationMethod_6,
                                                            mutualInfoRegistrationMethod=mutualInfoRegistrationMethod_6,
                                                            xSampling=xSampling_6,
                                                            ySampling=ySampling_6,
                                                            zSampling=zSampling_6,
                                                            mask=mask_6,
                                                            useMultiScale=useMultiScale_6)

# ----- BEGIN RETURNED VALUES DEFINITION ----- #
# transformationMatrix_6 = orsMatrix(0.99999999999957767, 1.2524462060314141e-07, -9.1039453429826028e-07, 4.9749051878912598e-08, -1.2524474831050215e-07, 0.99999999999998179, -1.4030722600422152e-07, 9.0149088298463464e-09, 9.1039451673071564e-07, 1.40307339968615e-07, 0.99999999999957545, -9.7965781598041701e-09, 0, 0, 0, 1)

# ----- END RETURNED VALUES DEFINITION ----- #
# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Register a moving dataset with a fixed dataset.

:name: register
:execution: execute

:param fixedChannel: reference dataset (fixed in space).
:type fixedChannel: ORSModel.ors.Channel
:param movingChannel: moving dataset.
:type movingChannel: ORSModel.ors.Channel
:param useScale_7: if True, the scale factor will be used.
:type useScale_7: bool
:param useRotation_7: if True, the rotation factor will be used.
:type useRotation_7: bool
:param useTranslation_7: if True, the translation factor will be used.
:type useTranslation_7: bool
:param xScaleInitial_7: initial value for the scale factor in the X direction
:type xScaleInitial_7: float
:param yScaleInitial_7: initial value for the scale factor in the Y direction
:type yScaleInitial_7: float
:param zScaleInitial_7: initial value for the scale factor in the Z direction
:type zScaleInitial_7: float
:param xRotationInitial_7: initial value for the rotation factor in the X direction
:type xRotationInitial_7: float
:param yRotationInitial_7: initial value for the rotation factor in the Y direction
:type yRotationInitial_7: float
:param zRotationInitial_7: initial value for the rotation factor in the Z direction
:type zRotationInitial_7: float
:param xTranslationInitial_7: initial value for the translation factor in the X direction
:type xTranslationInitial_7: float
:param yTranslationInitial_7: initial value for the translation factor in the Y direction
:type yTranslationInitial_7: float
:param zTranslationInitial_7: initial value for the translation factor in the Z direction
:type zTranslationInitial_7: float
:param xScaleSmallest_7: final value for the scale factor in the X direction
:type xScaleSmallest_7: float
:param yScaleSmallest_7: final value for the scale factor in the Y direction
:type yScaleSmallest_7: float
:param zScaleSmallest_7: final value for the scale factor in the Z direction
:type zScaleSmallest_7: float
:param xRotationSmallest_7: final value for the rotation factor in the X direction
:type xRotationSmallest_7: float
:param yRotationSmallest_7: final value for the rotation factor in the Y direction
:type yRotationSmallest_7: float
:param zRotationSmallest_7: final value for the rotation factor in the Z direction
:type zRotationSmallest_7: float
:param xTranslationSmallest_7: final value for the translation factor in the X direction
:type xTranslationSmallest_7: float
:param yTranslationSmallest_7: final value for the translation factor in the Y direction
:type yTranslationSmallest_7: float
:param zTranslationSmallest_7: final value for the translation factor in the Z direction
:type zTranslationSmallest_7: float
:param nearestInterpolationMethod_7: if True, the nearest interpolation method will be used; if False, the linear interpolation will be used.
:type nearestInterpolationMethod_7: bool
:param mutualInfoRegistrationMethod_7: if True, the mutual information registration algorithm will be used; if False, the SSD registration algorithm will be used.
:type mutualInfoRegistrationMethod_7: bool
:param xSampling_7: sampling in the X direction for the similarity metric
:type xSampling_7: int
:param ySampling_7: sampling in the Y direction for the similarity metric
:type ySampling_7: int
:param zSampling_7: sampling in the Z direction for the similarity metric
:type zSampling_7: int
:param mask_7: Visual Shape 3D or ROI that mask pixels of fixed dataset to make a scored registration.
:type mask_7: ORSModel.ors.ROI, ORSModel.ors.VisualShape3D
:param useMultiScale_7: Use a multiscale step in the registration
:type useMultiScale_7: bool

:return transformationMatrix_7: transformation matrix to go from the original location of the moving dataset to the final location of the moving dataset
:rtype transformationMatrix_7: ORSModel.ors.Matrix4x4
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
useScale_7 = False

useRotation_7 = True

useTranslation_7 = True

xScaleInitial_7 = 0.1

yScaleInitial_7 = 0.1

zScaleInitial_7 = 0.1

xRotationInitial_7 = 0.08726646259971647

yRotationInitial_7 = 0.08726646259971647

zRotationInitial_7 = 0.08726646259971647

xTranslationInitial_7 = 0.0001

yTranslationInitial_7 = 0.0001

zTranslationInitial_7 = 0.0001

xScaleSmallest_7 = 0.001

yScaleSmallest_7 = 0.001

zScaleSmallest_7 = 0.001

xRotationSmallest_7 = 0.00017453292519943296

yRotationSmallest_7 = 0.00017453292519943296

zRotationSmallest_7 = 0.00017453292519943296

xTranslationSmallest_7 = 1e-05

yTranslationSmallest_7 = 1e-05

zTranslationSmallest_7 = 1e-05

nearestInterpolationMethod_7 = False

mutualInfoRegistrationMethod_7 = True

xSampling_7 = 1

ySampling_7 = 1

zSampling_7 = 1

mask_7 = None

useMultiScale_7 = True

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
transformationMatrix_7 = OrsRigidRegistrationModel.register(fixedChannel=fixedChannel,
                                                            movingChannel=movingChannel,
                                                            useScale=useScale_7,
                                                            useRotation=useRotation_7,
                                                            useTranslation=useTranslation_7,
                                                            xScaleInitial=xScaleInitial_7,
                                                            yScaleInitial=yScaleInitial_7,
                                                            zScaleInitial=zScaleInitial_7,
                                                            xRotationInitial=xRotationInitial_7,
                                                            yRotationInitial=yRotationInitial_7,
                                                            zRotationInitial=zRotationInitial_7,
                                                            xTranslationInitial=xTranslationInitial_7,
                                                            yTranslationInitial=yTranslationInitial_7,
                                                            zTranslationInitial=zTranslationInitial_7,
                                                            xScaleSmallest=xScaleSmallest_7,
                                                            yScaleSmallest=yScaleSmallest_7,
                                                            zScaleSmallest=zScaleSmallest_7,
                                                            xRotationSmallest=xRotationSmallest_7,
                                                            yRotationSmallest=yRotationSmallest_7,
                                                            zRotationSmallest=zRotationSmallest_7,
                                                            xTranslationSmallest=xTranslationSmallest_7,
                                                            yTranslationSmallest=yTranslationSmallest_7,
                                                            zTranslationSmallest=zTranslationSmallest_7,
                                                            nearestInterpolationMethod=nearestInterpolationMethod_7,
                                                            mutualInfoRegistrationMethod=mutualInfoRegistrationMethod_7,
                                                            xSampling=xSampling_7,
                                                            ySampling=ySampling_7,
                                                            zSampling=zSampling_7,
                                                            mask=mask_7,
                                                            useMultiScale=useMultiScale_7)

# ----- BEGIN RETURNED VALUES DEFINITION ----- #
# transformationMatrix_7 = orsMatrix(0.99999999999957812, 1.2524462063463748e-07, -9.1039453429999501e-07, 4.9749051874575789e-08, -1.2524474833901667e-07, 0.99999999999998246, -1.4030722594871037e-07, 9.0149088220400908e-09, 9.1039451672984828e-07, 1.4030733999637057e-07, 0.99999999999957589, -9.7965781806208518e-09, 0, 0, 0, 1)

# ----- END RETURNED VALUES DEFINITION ----- #
# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Register a moving dataset with a fixed dataset.

:name: register
:execution: execute

:param fixedChannel: reference dataset (fixed in space).
:type fixedChannel: ORSModel.ors.Channel
:param movingChannel: moving dataset.
:type movingChannel: ORSModel.ors.Channel
:param useScale_8: if True, the scale factor will be used.
:type useScale_8: bool
:param useRotation_8: if True, the rotation factor will be used.
:type useRotation_8: bool
:param useTranslation_8: if True, the translation factor will be used.
:type useTranslation_8: bool
:param xScaleInitial_8: initial value for the scale factor in the X direction
:type xScaleInitial_8: float
:param yScaleInitial_8: initial value for the scale factor in the Y direction
:type yScaleInitial_8: float
:param zScaleInitial_8: initial value for the scale factor in the Z direction
:type zScaleInitial_8: float
:param xRotationInitial_8: initial value for the rotation factor in the X direction
:type xRotationInitial_8: float
:param yRotationInitial_8: initial value for the rotation factor in the Y direction
:type yRotationInitial_8: float
:param zRotationInitial_8: initial value for the rotation factor in the Z direction
:type zRotationInitial_8: float
:param xTranslationInitial_8: initial value for the translation factor in the X direction
:type xTranslationInitial_8: float
:param yTranslationInitial_8: initial value for the translation factor in the Y direction
:type yTranslationInitial_8: float
:param zTranslationInitial_8: initial value for the translation factor in the Z direction
:type zTranslationInitial_8: float
:param xScaleSmallest_8: final value for the scale factor in the X direction
:type xScaleSmallest_8: float
:param yScaleSmallest_8: final value for the scale factor in the Y direction
:type yScaleSmallest_8: float
:param zScaleSmallest_8: final value for the scale factor in the Z direction
:type zScaleSmallest_8: float
:param xRotationSmallest_8: final value for the rotation factor in the X direction
:type xRotationSmallest_8: float
:param yRotationSmallest_8: final value for the rotation factor in the Y direction
:type yRotationSmallest_8: float
:param zRotationSmallest_8: final value for the rotation factor in the Z direction
:type zRotationSmallest_8: float
:param xTranslationSmallest_8: final value for the translation factor in the X direction
:type xTranslationSmallest_8: float
:param yTranslationSmallest_8: final value for the translation factor in the Y direction
:type yTranslationSmallest_8: float
:param zTranslationSmallest_8: final value for the translation factor in the Z direction
:type zTranslationSmallest_8: float
:param nearestInterpolationMethod_8: if True, the nearest interpolation method will be used; if False, the linear interpolation will be used.
:type nearestInterpolationMethod_8: bool
:param mutualInfoRegistrationMethod_8: if True, the mutual information registration algorithm will be used; if False, the SSD registration algorithm will be used.
:type mutualInfoRegistrationMethod_8: bool
:param xSampling_8: sampling in the X direction for the similarity metric
:type xSampling_8: int
:param ySampling_8: sampling in the Y direction for the similarity metric
:type ySampling_8: int
:param zSampling_8: sampling in the Z direction for the similarity metric
:type zSampling_8: int
:param mask_8: Visual Shape 3D or ROI that mask pixels of fixed dataset to make a scored registration.
:type mask_8: ORSModel.ors.ROI, ORSModel.ors.VisualShape3D
:param useMultiScale_8: Use a multiscale step in the registration
:type useMultiScale_8: bool

:return transformationMatrix_8: transformation matrix to go from the original location of the moving dataset to the final location of the moving dataset
:rtype transformationMatrix_8: ORSModel.ors.Matrix4x4
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
useScale_8 = False

useRotation_8 = True

useTranslation_8 = True

xScaleInitial_8 = 0.1

yScaleInitial_8 = 0.1

zScaleInitial_8 = 0.1

xRotationInitial_8 = 0.08726646259971647

yRotationInitial_8 = 0.08726646259971647

zRotationInitial_8 = 0.08726646259971647

xTranslationInitial_8 = 0.0001

yTranslationInitial_8 = 0.0001

zTranslationInitial_8 = 0.0001

xScaleSmallest_8 = 0.001

yScaleSmallest_8 = 0.001

zScaleSmallest_8 = 0.001

xRotationSmallest_8 = 0.00017453292519943296

yRotationSmallest_8 = 0.00017453292519943296

zRotationSmallest_8 = 0.00017453292519943296

xTranslationSmallest_8 = 1e-05

yTranslationSmallest_8 = 1e-05

zTranslationSmallest_8 = 1e-05

nearestInterpolationMethod_8 = False

mutualInfoRegistrationMethod_8 = True

xSampling_8 = 1

ySampling_8 = 1

zSampling_8 = 1

mask_8 = None

useMultiScale_8 = True

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
transformationMatrix_8 = OrsRigidRegistrationModel.register(fixedChannel=fixedChannel,
                                                            movingChannel=movingChannel,
                                                            useScale=useScale_8,
                                                            useRotation=useRotation_8,
                                                            useTranslation=useTranslation_8,
                                                            xScaleInitial=xScaleInitial_8,
                                                            yScaleInitial=yScaleInitial_8,
                                                            zScaleInitial=zScaleInitial_8,
                                                            xRotationInitial=xRotationInitial_8,
                                                            yRotationInitial=yRotationInitial_8,
                                                            zRotationInitial=zRotationInitial_8,
                                                            xTranslationInitial=xTranslationInitial_8,
                                                            yTranslationInitial=yTranslationInitial_8,
                                                            zTranslationInitial=zTranslationInitial_8,
                                                            xScaleSmallest=xScaleSmallest_8,
                                                            yScaleSmallest=yScaleSmallest_8,
                                                            zScaleSmallest=zScaleSmallest_8,
                                                            xRotationSmallest=xRotationSmallest_8,
                                                            yRotationSmallest=yRotationSmallest_8,
                                                            zRotationSmallest=zRotationSmallest_8,
                                                            xTranslationSmallest=xTranslationSmallest_8,
                                                            yTranslationSmallest=yTranslationSmallest_8,
                                                            zTranslationSmallest=zTranslationSmallest_8,
                                                            nearestInterpolationMethod=nearestInterpolationMethod_8,
                                                            mutualInfoRegistrationMethod=mutualInfoRegistrationMethod_8,
                                                            xSampling=xSampling_8,
                                                            ySampling=ySampling_8,
                                                            zSampling=zSampling_8,
                                                            mask=mask_8,
                                                            useMultiScale=useMultiScale_8)

# ----- BEGIN RETURNED VALUES DEFINITION ----- #
# transformationMatrix_8 = orsMatrix(0.99999999999957734, 1.2524462057934317e-07, -9.1039453429695924e-07, 4.9749051884116768e-08, -1.252447483166279e-07, 0.99999999999998246, -1.4030722603197709e-07, 9.0149088263768995e-09, 9.1039451672984828e-07, 1.4030733999637057e-07, 0.99999999999957567, -9.796578166743064e-09, 0, 0, 0, 1)

# ----- END RETURNED VALUES DEFINITION ----- #
# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Register a moving dataset with a fixed dataset.

:name: register
:execution: execute

:param fixedChannel: reference dataset (fixed in space).
:type fixedChannel: ORSModel.ors.Channel
:param movingChannel: moving dataset.
:type movingChannel: ORSModel.ors.Channel
:param useScale_9: if True, the scale factor will be used.
:type useScale_9: bool
:param useRotation_9: if True, the rotation factor will be used.
:type useRotation_9: bool
:param useTranslation_9: if True, the translation factor will be used.
:type useTranslation_9: bool
:param xScaleInitial_9: initial value for the scale factor in the X direction
:type xScaleInitial_9: float
:param yScaleInitial_9: initial value for the scale factor in the Y direction
:type yScaleInitial_9: float
:param zScaleInitial_9: initial value for the scale factor in the Z direction
:type zScaleInitial_9: float
:param xRotationInitial_9: initial value for the rotation factor in the X direction
:type xRotationInitial_9: float
:param yRotationInitial_9: initial value for the rotation factor in the Y direction
:type yRotationInitial_9: float
:param zRotationInitial_9: initial value for the rotation factor in the Z direction
:type zRotationInitial_9: float
:param xTranslationInitial_9: initial value for the translation factor in the X direction
:type xTranslationInitial_9: float
:param yTranslationInitial_9: initial value for the translation factor in the Y direction
:type yTranslationInitial_9: float
:param zTranslationInitial_9: initial value for the translation factor in the Z direction
:type zTranslationInitial_9: float
:param xScaleSmallest_9: final value for the scale factor in the X direction
:type xScaleSmallest_9: float
:param yScaleSmallest_9: final value for the scale factor in the Y direction
:type yScaleSmallest_9: float
:param zScaleSmallest_9: final value for the scale factor in the Z direction
:type zScaleSmallest_9: float
:param xRotationSmallest_9: final value for the rotation factor in the X direction
:type xRotationSmallest_9: float
:param yRotationSmallest_9: final value for the rotation factor in the Y direction
:type yRotationSmallest_9: float
:param zRotationSmallest_9: final value for the rotation factor in the Z direction
:type zRotationSmallest_9: float
:param xTranslationSmallest_9: final value for the translation factor in the X direction
:type xTranslationSmallest_9: float
:param yTranslationSmallest_9: final value for the translation factor in the Y direction
:type yTranslationSmallest_9: float
:param zTranslationSmallest_9: final value for the translation factor in the Z direction
:type zTranslationSmallest_9: float
:param nearestInterpolationMethod_9: if True, the nearest interpolation method will be used; if False, the linear interpolation will be used.
:type nearestInterpolationMethod_9: bool
:param mutualInfoRegistrationMethod_9: if True, the mutual information registration algorithm will be used; if False, the SSD registration algorithm will be used.
:type mutualInfoRegistrationMethod_9: bool
:param xSampling_9: sampling in the X direction for the similarity metric
:type xSampling_9: int
:param ySampling_9: sampling in the Y direction for the similarity metric
:type ySampling_9: int
:param zSampling_9: sampling in the Z direction for the similarity metric
:type zSampling_9: int
:param mask_9: Visual Shape 3D or ROI that mask pixels of fixed dataset to make a scored registration.
:type mask_9: ORSModel.ors.ROI, ORSModel.ors.VisualShape3D
:param useMultiScale_9: Use a multiscale step in the registration
:type useMultiScale_9: bool

:return transformationMatrix_9: transformation matrix to go from the original location of the moving dataset to the final location of the moving dataset
:rtype transformationMatrix_9: ORSModel.ors.Matrix4x4
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
useScale_9 = False

useRotation_9 = True

useTranslation_9 = True

xScaleInitial_9 = 0.1

yScaleInitial_9 = 0.1

zScaleInitial_9 = 0.1

xRotationInitial_9 = 0.08726646259971647

yRotationInitial_9 = 0.08726646259971647

zRotationInitial_9 = 0.08726646259971647

xTranslationInitial_9 = 0.0001

yTranslationInitial_9 = 0.0001

zTranslationInitial_9 = 0.0001

xScaleSmallest_9 = 0.001

yScaleSmallest_9 = 0.001

zScaleSmallest_9 = 0.001

xRotationSmallest_9 = 0.00017453292519943296

yRotationSmallest_9 = 0.00017453292519943296

zRotationSmallest_9 = 0.00017453292519943296

xTranslationSmallest_9 = 1e-05

yTranslationSmallest_9 = 1e-05

zTranslationSmallest_9 = 1e-05

nearestInterpolationMethod_9 = False

mutualInfoRegistrationMethod_9 = True

xSampling_9 = 1

ySampling_9 = 1

zSampling_9 = 1

mask_9 = None

useMultiScale_9 = True

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
transformationMatrix_9 = OrsRigidRegistrationModel.register(fixedChannel=fixedChannel,
                                                            movingChannel=movingChannel,
                                                            useScale=useScale_9,
                                                            useRotation=useRotation_9,
                                                            useTranslation=useTranslation_9,
                                                            xScaleInitial=xScaleInitial_9,
                                                            yScaleInitial=yScaleInitial_9,
                                                            zScaleInitial=zScaleInitial_9,
                                                            xRotationInitial=xRotationInitial_9,
                                                            yRotationInitial=yRotationInitial_9,
                                                            zRotationInitial=zRotationInitial_9,
                                                            xTranslationInitial=xTranslationInitial_9,
                                                            yTranslationInitial=yTranslationInitial_9,
                                                            zTranslationInitial=zTranslationInitial_9,
                                                            xScaleSmallest=xScaleSmallest_9,
                                                            yScaleSmallest=yScaleSmallest_9,
                                                            zScaleSmallest=zScaleSmallest_9,
                                                            xRotationSmallest=xRotationSmallest_9,
                                                            yRotationSmallest=yRotationSmallest_9,
                                                            zRotationSmallest=zRotationSmallest_9,
                                                            xTranslationSmallest=xTranslationSmallest_9,
                                                            yTranslationSmallest=yTranslationSmallest_9,
                                                            zTranslationSmallest=zTranslationSmallest_9,
                                                            nearestInterpolationMethod=nearestInterpolationMethod_9,
                                                            mutualInfoRegistrationMethod=mutualInfoRegistrationMethod_9,
                                                            xSampling=xSampling_9,
                                                            ySampling=ySampling_9,
                                                            zSampling=zSampling_9,
                                                            mask=mask_9,
                                                            useMultiScale=useMultiScale_9)

# ----- BEGIN RETURNED VALUES DEFINITION ----- #
# transformationMatrix_9 = orsMatrix(0.99999998547454527, -0.00016874458431822089, -2.400364400291467e-05, 2.9267029824078458e-06, 0.00016874456862958436, 0.99999998576242055, -6.5561633805222286e-07, -1.5349223317327743e-06, 2.400375429287803e-05, 6.51565843889923e-07, 0.99999999971169773, -2.2967660159856074e-07, 0, 0, 0, 0.99999999999999989)

# ----- END RETURNED VALUES DEFINITION ----- #
# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Register a moving dataset with a fixed dataset.

:name: register
:execution: execute

:param fixedChannel: reference dataset (fixed in space).
:type fixedChannel: ORSModel.ors.Channel
:param movingChannel: moving dataset.
:type movingChannel: ORSModel.ors.Channel
:param useScale_10: if True, the scale factor will be used.
:type useScale_10: bool
:param useRotation_10: if True, the rotation factor will be used.
:type useRotation_10: bool
:param useTranslation_10: if True, the translation factor will be used.
:type useTranslation_10: bool
:param xScaleInitial_10: initial value for the scale factor in the X direction
:type xScaleInitial_10: float
:param yScaleInitial_10: initial value for the scale factor in the Y direction
:type yScaleInitial_10: float
:param zScaleInitial_10: initial value for the scale factor in the Z direction
:type zScaleInitial_10: float
:param xRotationInitial_10: initial value for the rotation factor in the X direction
:type xRotationInitial_10: float
:param yRotationInitial_10: initial value for the rotation factor in the Y direction
:type yRotationInitial_10: float
:param zRotationInitial_10: initial value for the rotation factor in the Z direction
:type zRotationInitial_10: float
:param xTranslationInitial_10: initial value for the translation factor in the X direction
:type xTranslationInitial_10: float
:param yTranslationInitial_10: initial value for the translation factor in the Y direction
:type yTranslationInitial_10: float
:param zTranslationInitial_10: initial value for the translation factor in the Z direction
:type zTranslationInitial_10: float
:param xScaleSmallest_10: final value for the scale factor in the X direction
:type xScaleSmallest_10: float
:param yScaleSmallest_10: final value for the scale factor in the Y direction
:type yScaleSmallest_10: float
:param zScaleSmallest_10: final value for the scale factor in the Z direction
:type zScaleSmallest_10: float
:param xRotationSmallest_10: final value for the rotation factor in the X direction
:type xRotationSmallest_10: float
:param yRotationSmallest_10: final value for the rotation factor in the Y direction
:type yRotationSmallest_10: float
:param zRotationSmallest_10: final value for the rotation factor in the Z direction
:type zRotationSmallest_10: float
:param xTranslationSmallest_10: final value for the translation factor in the X direction
:type xTranslationSmallest_10: float
:param yTranslationSmallest_10: final value for the translation factor in the Y direction
:type yTranslationSmallest_10: float
:param zTranslationSmallest_10: final value for the translation factor in the Z direction
:type zTranslationSmallest_10: float
:param nearestInterpolationMethod_10: if True, the nearest interpolation method will be used; if False, the linear interpolation will be used.
:type nearestInterpolationMethod_10: bool
:param mutualInfoRegistrationMethod_10: if True, the mutual information registration algorithm will be used; if False, the SSD registration algorithm will be used.
:type mutualInfoRegistrationMethod_10: bool
:param xSampling_10: sampling in the X direction for the similarity metric
:type xSampling_10: int
:param ySampling_10: sampling in the Y direction for the similarity metric
:type ySampling_10: int
:param zSampling_10: sampling in the Z direction for the similarity metric
:type zSampling_10: int
:param mask_10: Visual Shape 3D or ROI that mask pixels of fixed dataset to make a scored registration.
:type mask_10: ORSModel.ors.ROI, ORSModel.ors.VisualShape3D
:param useMultiScale_10: Use a multiscale step in the registration
:type useMultiScale_10: bool

:return transformationMatrix_10: transformation matrix to go from the original location of the moving dataset to the final location of the moving dataset
:rtype transformationMatrix_10: ORSModel.ors.Matrix4x4
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
useScale_10 = False

useRotation_10 = True

useTranslation_10 = True

xScaleInitial_10 = 0.1

yScaleInitial_10 = 0.1

zScaleInitial_10 = 0.1

xRotationInitial_10 = 0.08726646259971647

yRotationInitial_10 = 0.08726646259971647

zRotationInitial_10 = 0.08726646259971647

xTranslationInitial_10 = 0.0001

yTranslationInitial_10 = 0.0001

zTranslationInitial_10 = 0.0001

xScaleSmallest_10 = 0.001

yScaleSmallest_10 = 0.001

zScaleSmallest_10 = 0.001

xRotationSmallest_10 = 0.00017453292519943296

yRotationSmallest_10 = 0.00017453292519943296

zRotationSmallest_10 = 0.00017453292519943296

xTranslationSmallest_10 = 1e-06

yTranslationSmallest_10 = 1e-06

zTranslationSmallest_10 = 1e-06

nearestInterpolationMethod_10 = False

mutualInfoRegistrationMethod_10 = True

xSampling_10 = 1

ySampling_10 = 1

zSampling_10 = 1

mask_10 = None

useMultiScale_10 = True

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
transformationMatrix_10 = OrsRigidRegistrationModel.register(fixedChannel=fixedChannel,
                                                             movingChannel=movingChannel,
                                                             useScale=useScale_10,
                                                             useRotation=useRotation_10,
                                                             useTranslation=useTranslation_10,
                                                             xScaleInitial=xScaleInitial_10,
                                                             yScaleInitial=yScaleInitial_10,
                                                             zScaleInitial=zScaleInitial_10,
                                                             xRotationInitial=xRotationInitial_10,
                                                             yRotationInitial=yRotationInitial_10,
                                                             zRotationInitial=zRotationInitial_10,
                                                             xTranslationInitial=xTranslationInitial_10,
                                                             yTranslationInitial=yTranslationInitial_10,
                                                             zTranslationInitial=zTranslationInitial_10,
                                                             xScaleSmallest=xScaleSmallest_10,
                                                             yScaleSmallest=yScaleSmallest_10,
                                                             zScaleSmallest=zScaleSmallest_10,
                                                             xRotationSmallest=xRotationSmallest_10,
                                                             yRotationSmallest=yRotationSmallest_10,
                                                             zRotationSmallest=zRotationSmallest_10,
                                                             xTranslationSmallest=xTranslationSmallest_10,
                                                             yTranslationSmallest=yTranslationSmallest_10,
                                                             zTranslationSmallest=zTranslationSmallest_10,
                                                             nearestInterpolationMethod=nearestInterpolationMethod_10,
                                                             mutualInfoRegistrationMethod=mutualInfoRegistrationMethod_10,
                                                             xSampling=xSampling_10,
                                                             ySampling=ySampling_10,
                                                             zSampling=zSampling_10,
                                                             mask=mask_10,
                                                             useMultiScale=useMultiScale_10)

# ----- BEGIN RETURNED VALUES DEFINITION ----- #
# transformationMatrix_10 = orsMatrix(0.99999918892001727, -0.0007173216750495572, -0.0010524300084609481, 6.4833100871325433e-05, 0.00071789287788770321, 0.99999959517836179, 0.00054246928758092117, -3.6931918312970401e-05, 0.0010520404574364851, -0.00054322437960266368, 0.99999929905882923, -6.2226235458887058e-06, 0, 0, 0, 1)

# ----- END RETURNED VALUES DEFINITION ----- #
# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Register a moving dataset with a fixed dataset.

:name: register
:execution: execute

:param fixedChannel: reference dataset (fixed in space).
:type fixedChannel: ORSModel.ors.Channel
:param movingChannel: moving dataset.
:type movingChannel: ORSModel.ors.Channel
:param useScale_11: if True, the scale factor will be used.
:type useScale_11: bool
:param useRotation_11: if True, the rotation factor will be used.
:type useRotation_11: bool
:param useTranslation_11: if True, the translation factor will be used.
:type useTranslation_11: bool
:param xScaleInitial_11: initial value for the scale factor in the X direction
:type xScaleInitial_11: float
:param yScaleInitial_11: initial value for the scale factor in the Y direction
:type yScaleInitial_11: float
:param zScaleInitial_11: initial value for the scale factor in the Z direction
:type zScaleInitial_11: float
:param xRotationInitial_11: initial value for the rotation factor in the X direction
:type xRotationInitial_11: float
:param yRotationInitial_11: initial value for the rotation factor in the Y direction
:type yRotationInitial_11: float
:param zRotationInitial_11: initial value for the rotation factor in the Z direction
:type zRotationInitial_11: float
:param xTranslationInitial_11: initial value for the translation factor in the X direction
:type xTranslationInitial_11: float
:param yTranslationInitial_11: initial value for the translation factor in the Y direction
:type yTranslationInitial_11: float
:param zTranslationInitial_11: initial value for the translation factor in the Z direction
:type zTranslationInitial_11: float
:param xScaleSmallest_11: final value for the scale factor in the X direction
:type xScaleSmallest_11: float
:param yScaleSmallest_11: final value for the scale factor in the Y direction
:type yScaleSmallest_11: float
:param zScaleSmallest_11: final value for the scale factor in the Z direction
:type zScaleSmallest_11: float
:param xRotationSmallest_11: final value for the rotation factor in the X direction
:type xRotationSmallest_11: float
:param yRotationSmallest_11: final value for the rotation factor in the Y direction
:type yRotationSmallest_11: float
:param zRotationSmallest_11: final value for the rotation factor in the Z direction
:type zRotationSmallest_11: float
:param xTranslationSmallest_11: final value for the translation factor in the X direction
:type xTranslationSmallest_11: float
:param yTranslationSmallest_11: final value for the translation factor in the Y direction
:type yTranslationSmallest_11: float
:param zTranslationSmallest_11: final value for the translation factor in the Z direction
:type zTranslationSmallest_11: float
:param nearestInterpolationMethod_11: if True, the nearest interpolation method will be used; if False, the linear interpolation will be used.
:type nearestInterpolationMethod_11: bool
:param mutualInfoRegistrationMethod_11: if True, the mutual information registration algorithm will be used; if False, the SSD registration algorithm will be used.
:type mutualInfoRegistrationMethod_11: bool
:param xSampling_11: sampling in the X direction for the similarity metric
:type xSampling_11: int
:param ySampling_11: sampling in the Y direction for the similarity metric
:type ySampling_11: int
:param zSampling_11: sampling in the Z direction for the similarity metric
:type zSampling_11: int
:param mask_11: Visual Shape 3D or ROI that mask pixels of fixed dataset to make a scored registration.
:type mask_11: ORSModel.ors.ROI, ORSModel.ors.VisualShape3D
:param useMultiScale_11: Use a multiscale step in the registration
:type useMultiScale_11: bool

:return transformationMatrix_11: transformation matrix to go from the original location of the moving dataset to the final location of the moving dataset
:rtype transformationMatrix_11: ORSModel.ors.Matrix4x4
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
useScale_11 = False

useRotation_11 = True

useTranslation_11 = True

xScaleInitial_11 = 0.1

yScaleInitial_11 = 0.1

zScaleInitial_11 = 0.1

xRotationInitial_11 = 0.08726646259971647

yRotationInitial_11 = 0.08726646259971647

zRotationInitial_11 = 0.08726646259971647

xTranslationInitial_11 = 0.0001

yTranslationInitial_11 = 0.0001

zTranslationInitial_11 = 0.0001

xScaleSmallest_11 = 0.001

yScaleSmallest_11 = 0.001

zScaleSmallest_11 = 0.001

xRotationSmallest_11 = 0.00017453292519943296

yRotationSmallest_11 = 0.00017453292519943296

zRotationSmallest_11 = 0.00017453292519943296

xTranslationSmallest_11 = 1e-06

yTranslationSmallest_11 = 1e-06

zTranslationSmallest_11 = 1e-06

nearestInterpolationMethod_11 = False

mutualInfoRegistrationMethod_11 = True

xSampling_11 = 1

ySampling_11 = 1

zSampling_11 = 1

mask_11 = None

useMultiScale_11 = True

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
transformationMatrix_11 = OrsRigidRegistrationModel.register(fixedChannel=fixedChannel,
                                                             movingChannel=movingChannel,
                                                             useScale=useScale_11,
                                                             useRotation=useRotation_11,
                                                             useTranslation=useTranslation_11,
                                                             xScaleInitial=xScaleInitial_11,
                                                             yScaleInitial=yScaleInitial_11,
                                                             zScaleInitial=zScaleInitial_11,
                                                             xRotationInitial=xRotationInitial_11,
                                                             yRotationInitial=yRotationInitial_11,
                                                             zRotationInitial=zRotationInitial_11,
                                                             xTranslationInitial=xTranslationInitial_11,
                                                             yTranslationInitial=yTranslationInitial_11,
                                                             zTranslationInitial=zTranslationInitial_11,
                                                             xScaleSmallest=xScaleSmallest_11,
                                                             yScaleSmallest=yScaleSmallest_11,
                                                             zScaleSmallest=zScaleSmallest_11,
                                                             xRotationSmallest=xRotationSmallest_11,
                                                             yRotationSmallest=yRotationSmallest_11,
                                                             zRotationSmallest=zRotationSmallest_11,
                                                             xTranslationSmallest=xTranslationSmallest_11,
                                                             yTranslationSmallest=yTranslationSmallest_11,
                                                             zTranslationSmallest=zTranslationSmallest_11,
                                                             nearestInterpolationMethod=nearestInterpolationMethod_11,
                                                             mutualInfoRegistrationMethod=mutualInfoRegistrationMethod_11,
                                                             xSampling=xSampling_11,
                                                             ySampling=ySampling_11,
                                                             zSampling=zSampling_11,
                                                             mask=mask_11,
                                                             useMultiScale=useMultiScale_11)

# ----- BEGIN RETURNED VALUES DEFINITION ----- #
# transformationMatrix_11 = orsMatrix(0.99999999999999989, 8.1315162936412833e-19, 2.1684043449710089e-18, -1.7347234759768071e-18, 2.8460307027744491e-17, 1, -2.7755575615628914e-17, 1.7347234759768071e-18, -2.1684043449710089e-18, 2.7755575615628914e-17, 0.99999999999999967, 2.0816681711721685e-17, 0, 0, 0, 1)

# ----- END RETURNED VALUES DEFINITION ----- #
# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Resets the visual box of a Channel

:name: resetVisualBoxOfChannelFromLayoutGenealogicalName
:execution: execute
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
useScale_12 = False

useRotation_12 = True

useTranslation_12 = True

xScaleInitial_12 = 0.1

yScaleInitial_12 = 0.1

zScaleInitial_12 = 0.1

xRotationInitial_12 = 0.08726646259971647

yRotationInitial_12 = 0.08726646259971647

zRotationInitial_12 = 0.08726646259971647

xTranslationInitial_12 = 0.0001

yTranslationInitial_12 = 0.0001

zTranslationInitial_12 = 0.0001

xScaleSmallest_12 = 0.001

yScaleSmallest_12 = 0.001

zScaleSmallest_12 = 0.001

xRotationSmallest_12 = 0.00017453292519943296

yRotationSmallest_12 = 0.00017453292519943296

zRotationSmallest_12 = 0.00017453292519943296

xTranslationSmallest_12 = 1e-06

yTranslationSmallest_12 = 1e-06

zTranslationSmallest_12 = 1e-06

nearestInterpolationMethod_12 = False

mutualInfoRegistrationMethod_12 = True

xSampling_12 = 1

ySampling_12 = 1

zSampling_12 = 1

mask_12 = None

useMultiScale_12 = True

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
OrsRigidRegistrationModel.register(fixedChannel=fixedChannel,
                                   movingChannel=movingChannel,
                                   useScale=useScale_12,
                                   useRotation=useRotation_12,
                                   useTranslation=useTranslation_12,
                                   xScaleInitial=xScaleInitial_12,
                                   yScaleInitial=yScaleInitial_12,
                                   zScaleInitial=zScaleInitial_12,
                                   xRotationInitial=xRotationInitial_12,
                                   yRotationInitial=yRotationInitial_12,
                                   zRotationInitial=zRotationInitial_12,
                                   xTranslationInitial=xTranslationInitial_12,
                                   yTranslationInitial=yTranslationInitial_12,
                                   zTranslationInitial=zTranslationInitial_12,
                                   xScaleSmallest=xScaleSmallest_12,
                                   yScaleSmallest=yScaleSmallest_12,
                                   zScaleSmallest=zScaleSmallest_12,
                                   xRotationSmallest=xRotationSmallest_12,
                                   yRotationSmallest=yRotationSmallest_12,
                                   zRotationSmallest=zRotationSmallest_12,
                                   xTranslationSmallest=xTranslationSmallest_12,
                                   yTranslationSmallest=yTranslationSmallest_12,
                                   zTranslationSmallest=zTranslationSmallest_12,
                                   nearestInterpolationMethod=nearestInterpolationMethod_12,
                                   mutualInfoRegistrationMethod=mutualInfoRegistrationMethod_12,
                                   xSampling=xSampling_12,
                                   ySampling=ySampling_12,
                                   zSampling=zSampling_12,
                                   mask=mask_12,
                                   useMultiScale=useMultiScale_12)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Resets the visual box of a Channel

:name: resetVisualBoxOfChannelFromLayoutGenealogicalName
:execution: execute

:param aName: a genealogical name
:type aName: str
:param movingChannel: a Channel
:type movingChannel: ORSModel.ors.Channel
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
aName = ''

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
StructuredGridLogger.resetVisualBoxOfChannelFromLayoutGenealogicalName(aName=aName,
                                                                       channel=movingChannel)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Resets the visual box of a Channel

:name: resetVisualBoxOfChannelFromLayoutGenealogicalName
:execution: execute

:param aName_2: a genealogical name
:type aName_2: str
:param movingChannel: a Channel
:type movingChannel: ORSModel.ors.Channel
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
aName_2 = ''

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
StructuredGridLogger.resetVisualBoxOfChannelFromLayoutGenealogicalName(aName=aName_2,
                                                                       channel=movingChannel)

# ********** END MACRO ********** #

