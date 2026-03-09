clc 
clear all 
close all 
%% Initialization 
Folder="624" % >>> Enter your sample number <<<< (which is also the folder name containing the binary files for this sample)

directory='C:/Users/username/Box/..../Experimental_Folder/Samples/'; %direcotry of the binary files for the Midshaft, distal, or proximal ROI

days =18; % >>>> Enter the number of days between Pre and Post scans <<<< (to calculate rates) according to your experiment 

Mid=0; % >>> what region are you processing ? change from 0 to 1 <<<< 
Distal=1;
Prox=0; 
% Trab_only=1; % Need Prox =1 to work

nowing=0; % change to 1 if the tibial ridge has been removed 

starting_slice=1; %define the first slice of the stack to be analyzed
size_ROI=100; % number of slices included in the region to be analyzed 

pixel_xy_um=10.5; % pixel size in xy
pixel_z_um=10.5; % voxel depth 
voxelVolume_um3 = pixel_xy_um^2 * pixel_z_um; % voxel volume

directory_excelfile='C:/Users/username/Box/..../Experimental_Folder/Meslier_Results_3DDynamicHisto_copy.xlsx'; %Excel file directory (results export)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% read image 
if Mid==1 && nowing==0
Data_Formation=tiffreadVolume(directory+ Folder + '/Mid/F.tiff'); % sometimes need to change to .tif or .tiff depending if saved from fiji or from dragonfly
Data_Resorption=tiffreadVolume(directory+ Folder + '/Mid/R.tiff');
Data_WholeBone=tiffreadVolume(directory+ Folder + '/Mid/WB.tiff');
Data_Prebone=tiffreadVolume(directory+ Folder + '/Mid/PreBone.tiff');
end
%
if Mid==1 && nowing==1
Data_Formation=tiffreadVolume(directory+ Folder + '/Mid/F_nowing.tif'); % sometimes need to change to .tif or .tiff depending if saved from fiji or from dragonfly
Data_Resorption=tiffreadVolume(directory+ Folder + '/Mid/R_nowing.tif');
Data_WholeBone=tiffreadVolume(directory+ Folder + '/Mid/WB_nowing.tif');
Data_Prebone=tiffreadVolume(directory+ Folder + '/Mid/PreBone_nowing.tif');
end
%
if Prox==1
Data_Formation=tiffreadVolume(directory+ Folder + '/Proxi/F.tiff');
Data_Resorption=tiffreadVolume(directory+ Folder + '/Proxi/R.tiff');
Data_WholeBone=tiffreadVolume(directory+ Folder + '/Proxi/WB.tiff');
Data_Prebone=tiffreadVolume(directory+ Folder + '/Proxi/PreBone.tiff');
end

if Distal==1
Data_Formation=tiffreadVolume(directory+ Folder + '/Distal/F.tiff');
Data_Resorption=tiffreadVolume(directory+ Folder + '/Distal/R.tiff');
Data_WholeBone=tiffreadVolume(directory+ Folder + '/Distal/WB.tiff');
Data_Prebone=tiffreadVolume(directory+ Folder + '/Distal/PreBone.tiff');
end

% define ROI (right now 101 slices, could be changed)
s_stack=size(Data_Prebone);
size_stack=s_stack(3);
cut=starting_slice;  % region to be analyzed (101 slices, 5 slices down from the first proximal image) change to 30 for distal
Data_Formation=Data_Formation(:,:,cut:cut+size_ROI);
Data_Resorption=Data_Resorption(:,:,cut:cut+size_ROI);
Data_WholeBone=Data_WholeBone(:,:,cut:cut+size_ROI);
PreBone=Data_Prebone(:,:,cut:cut+size_ROI);

% Use WholeBone Mask to create mask for Outer and Inner surfaces
start =1;
stop=length(Data_WholeBone(1,1,:));
Outer_perim=[];
voxelVolume_um3 = pixel_xy_um^2 * pixel_z_um;

Data_Whole_bin           = false(size(Data_WholeBone));
Data_WholeBone_nofibend  = false(size(Data_WholeBone));
PreBone_nofibend_3d      = false(size(PreBone));     % <-- store per-slice
Marrow_3d                = false(size(Data_WholeBone));
PreBoneFill_3d           = false(size(PreBone));     % outer surface mask


%initialization of parameters
se_1_d= strel('diamond',1);
se_1= strel('Disk',1);
se_1_sqr= strel('square',1);
se_2= strel('Disk',2);
se_3= strel('Disk',3);
se_3_sqr= strel('square',3);
se_4= strel('Disk',4);
se_5= strel('Disk',5); %define size of closing parameter (See below)
se_6= strel('Disk',6);
se_7= strel('Disk',7);
se_10= strel('Disk',10);

for i=start:stop

    Data_Whole_bin(:,:,i)=imbinarize(Data_WholeBone(:,:,i));
    Data_WholeBone_nofibend(:,:,i)=Data_Whole_bin(:,:,i);
    if Distal == 1 % if we are processing a distal tibia => removed the wing (fibula disconnection at the ankle)
        slice = Data_WholeBone_nofibend(:,:,i);
        maxErosion = 8;  % Max erosion iterations
        minAreaThreshold = 100; % Minimum size (pixels) to consider object real
        connected = true;
        radius = 1; % initialization 
    
        while connected && radius <= maxErosion 
            % Erode with increasing radius
            temp = imerode(slice, strel('disk', radius));
    
            % Label connected components
            cc = bwconncomp(temp, 8);
    
            % Measure component areas
            stats = regionprops(cc, 'Area');
            areas = [stats.Area];
    
            % Sort in descending order
            sortedAreas = sort(areas, 'descend');
    
            % Check if second-largest component is big enough
            if numel(sortedAreas) >= 2 && sortedAreas(2) > minAreaThreshold
                tibia = bwareafilt(temp, 1);  % Keep largest object
                restored = imdilate(tibia, strel('disk', radius));
                Data_WholeBone_nofibend(:,:,i) = restored;
                % fprintf('Valid separation at slice %d with erosion radius %d\n', i, radius);
                connected = false;
            else
                radius = radius + 1; % increase radius if needed until we reach maxerosion parameter
            end
        end
    end



    % % Apply the nofibend mask to PreBone
    % PreBone_nofibend = zeros(size(PreBone), 'like', PreBone); % preallocate same type
    % PreBone_nofibend (Data_WholeBone_nofibend) = PreBone(Data_WholeBone_nofibend);
    % PreBone_nofibend =imbinarize(PreBone_nofibend);
    maskSlice = logical(Data_WholeBone_nofibend(:,:,i));
    PreBone_nofibend(:,:,i) = logical(PreBone(:,:,i)) & maskSlice;

%

    I{i}=Data_WholeBone_nofibend(:,:,i); % we want to use whole bone to capture marrow space and outer surface


    I_closed{i}=imclose(I{i},strel('Disk',4)); % close cortical bone to avoid blood vessel/gaps
    I_inv{i}=~I_closed{i}; % invert the image (black -> white)
    % threshArea=100000;% only keep Marrow area and remove background (large white bloc)
    regions=regionprops(I_inv{i});
    regions_area_mat=[regions.Area];
    threshArea=max(regions_area_mat)-1;% define threshold to remove brackground
    Ma{i}= xor(I_inv{i}, bwareaopen(I_inv{i} , threshArea)); % Define Marrow space
    Ma_dilated{i}=imdilate(Ma{i},se_4); % dilated Marrow space
    I_fill{i}=I{i}+Ma_dilated{i}; % create a mask with cortical bone and fileld bone marrow space
    temp=I_fill{i};
    I_fill{i}=imclose(temp,strel('Disk',4)); % close any remaining gap
    

%

    Ma_sumPixel{i}=sum(Ma{i},"all"); %if the masking did not work because to large of a gap in the bone (blodd vessel) => Ma{i} does not have any pixel
    
    if i>1 & i<5
        if Ma_sumPixel{i}==0 | Ma_sumPixel{i}<0.25*Ma_sumPixel{1}% if no pixel in the image or if MA{i} smaller than expected compared to previous slide
        I_closed{i}=imclose(I{i},strel('Disk',6)); % use large radius to close the bone
        I_inv{i}=~I_closed{i};
        regions=regionprops(I_inv{i});
        regions_area_mat=[regions.Area];
        threshArea=max(regions_area_mat)-1;% define threshold to remove brackground 
        Ma{i}= xor(I_inv{i}, bwareaopen(I_inv{i} , threshArea));
        Area_Ma{i}=bwarea(Ma{i});
        Area_Ma_mat=cell2mat(Area_Ma);
        Ma_dilated{i}=imdilate(Ma{i},strel('Disk',4));
        I_fill{i}=I{i}+Ma{i};  
        I_fill{i}=imclose(I_fill{i},strel('Disk',4)); 
        end
    end

    radius_close=7; % define radius to close the bone gap
    closed=0; %condition to remove of the while loop
   
    if i>=5 
        % I_fill_sumPixel=sum(I_fill{i-3},"all"); %get the sum of pixel from the whole bone area from 4 slices away 
        if Ma_sumPixel{i}==0 | Ma_sumPixel{i}<0.50*Ma_sumPixel{i-3} % if the sum of pixel is inferior to 80% of the image located 3 slices away
            I_closed{i}=imclose(I{i},strel('Disk',radius_close)); % then use a larger radius to close the bone
            I_inv{i}=~I_closed{i};
            regions=regionprops(I_inv{i});
            regions_area_mat=[regions.Area];
            threshArea=max(regions_area_mat)-1;% define threshold to remove brackground 
            Ma{i}= xor(I_inv{i}, bwareaopen(I_inv{i} , threshArea));
            Area_Ma{i}=bwarea(Ma{i});
            Area_Ma_mat=cell2mat(Area_Ma);
            Ma_dilated{i}=imdilate(Ma{i},strel('Disk',4));
            I_fill{i}=I{i}+Ma{i};  
            I_fill{i}=imclose(I_fill{i},strel('Disk',4)); % close cortical bone to avoid blood vessel/gaps
            check{i}=1;
        end
    end

    % Remove thin connections (e.g., 1-pixel width)
    I_cleaned = bwareaopen(I_fill{i}, 10);  % removes small blobs
    I_cleaned = imerode(I_cleaned, strel('square', 2));  % erode to break connections
    I_cleaned = imdilate(I_cleaned, strel('square', 2)); % restore shape

    % Reassign cleaned image
    I_fill{i} = I_cleaned;
    
    % Get all regions
    regions_TibiaFib = regionprops("table", I_fill{i}, "Area", "PixelIdxList");
    
    % Find the largest region
    [~, idxLargest] = max(regions_TibiaFib.Area);
    
    % Create a blank mask
    I_largest = false(size(I_fill{i}));
    
    % Fill in only the largest region
    I_largest(regions_TibiaFib.PixelIdxList{idxLargest}) = true;
    
    % Overwrite or store result
    I_fill{i} = I_largest;
    I_intersect{i} = I_fill{i} & Ma{i};
    Ma{i}=I_intersect{i};
    Marrow_3d(:,:,i)      = logical(Ma{i});
    PreBoneFill_3d(:,:,i) = imfill(logical(PreBone_nofibend(:,:,i)),'holes');

    Outer_perim(:,:,i)=bwperim(I_fill{i}); % Outer perimeter is the outer perimeter of the bone
    Outer_perim_dilated(:,:,i)=imdilate(Outer_perim(:,:,i),se_6);
    
    Inner_perim(:,:,i)=bwperim(Ma{i}); % Inner perimeter is the outer perimeter of the marrow space
    Inner_perim_dilated(:,:,i)=imdilate(Inner_perim(:,:,i),se_6);
    
    
    stats_Outer_perim = regionprops(I_fill{i}, 'Perimeter'); % calculate perimeter 
    % Sum all perimeters for this slice (handles multiple regions, in case
    % there the bone marrow space is split
    total_outer_perim_px(i) = sum([stats_Outer_perim.Perimeter]);
    Outer_perimeter_length_px(i) = total_outer_perim_px(i);
    Outer_perimeter_length_um(i) = total_outer_perim_px(i) * pixel_xy_um;      % convert to microns
    
    stats_Inner_perim = regionprops(Ma{i}, 'Perimeter');% calculate perimeter 
    % Sum all perimeters for this slice (handles multiple regions)
    total_inner_perim_px(i) = sum([stats_Inner_perim.Perimeter]);
    Inner_perimeter_length_px(i) = total_inner_perim_px(i);
    Inner_perimeter_length_um(i) = total_inner_perim_px(i) * pixel_xy_um; 
    
    total_all_perim_px(i)=total_outer_perim_px(i) + total_inner_perim_px(i); % perimeter of endo + perio 

end

sx = pixel_xy_um; sy = pixel_xy_um; sz = pixel_z_um;

S_endo_um2  = surfaceArea_um2_fromMask(Marrow_3d, sx, sy, sz);      % endosteal
S_perio_um2 = surfaceArea_um2_fromMask(PreBoneFill_3d, sx, sy, sz); % periosteal

S_endo_mm2  = S_endo_um2  / 1e6;
S_perio_mm2 = S_perio_um2 / 1e6;

fprintf('Endosteal surface = %.3f um^2\n', S_endo_um2);
fprintf('Periosteal surface = %.3f um^2\n', S_perio_um2);


% APPLY MASKS — CONNECTED-COMPONENT EXPANSION
%  - initialCapture = Formation_bin & DilatedPerim
%  - keep any connected component of Formation that intersects initialCapture
% This extends the captured periosteal/endosteal regions to include bumps
% that are connected to the captured region.
%  - Any connected component captured in INNER is not allowed in OUTER.

j = 0;
min_keep_pixels = 3;

for i = start:stop

    % binarize formation/resorption slices
    Data_Formation_bin = imbinarize(Data_Formation(:,:,i));
    Data_Resorption_bin = imbinarize(Data_Resorption(:,:,i));

    % ===============================
    %  1) ---- INNER (ENDO) PROCESSING
    %  ===============================
    IP_dil = Inner_perim_dilated(:,:,i) > 0;

    % INNER formation initial capture
    initialCapture_inner = Data_Formation_bin & IP_dil;

    % Connected components of formation
    CC_F_inner = bwconncomp(Data_Formation_bin);
    finalCapture_inner = false(size(Data_Formation_bin));

    for k = 1:CC_F_inner.NumObjects
        pix = CC_F_inner.PixelIdxList{k};
        if any(initialCapture_inner(pix))
            finalCapture_inner(pix) = true;
        end
    end
    finalCapture_inner = bwareaopen(finalCapture_inner, min_keep_pixels);

    % INNER resorption
    initialCapture_inner_R = Data_Resorption_bin & IP_dil;
    CC_R_inner = bwconncomp(Data_Resorption_bin);
    finalCapture_inner_R = false(size(Data_Resorption_bin));

    for k = 1:CC_R_inner.NumObjects
        pix = CC_R_inner.PixelIdxList{k};
        if any(initialCapture_inner_R(pix))
            finalCapture_inner_R(pix) = true;
        end
    end
    finalCapture_inner_R = bwareaopen(finalCapture_inner_R, min_keep_pixels);

    % Save inner masks
    Inner_Formation(:,:,i)   = finalCapture_inner;
    Inner_Resorption(:,:,i)  = finalCapture_inner_R;

    % -------------------------------------------------------------
    % Create a mask of components already assigned to INNER
    % so we can exclude them from OUTER counts
    % -------------------------------------------------------------
    INNER_assigned_mask = finalCapture_inner | finalCapture_inner_R;


    % ===============================
    %  2) ---- OUTER (PERIO) PROCESSING
    %  ===============================
    OP_dil = Outer_perim_dilated(:,:,i) > 0;

    % OUTER formation initial capture
    initialCapture_outer = Data_Formation_bin & OP_dil;

    CC_F_outer = bwconncomp(Data_Formation_bin);
    finalCapture_outer = false(size(Data_Formation_bin));

    for k = 1:CC_F_outer.NumObjects
        pix = CC_F_outer.PixelIdxList{k};

        % SKIP if this component belongs to INNER
        if any(INNER_assigned_mask(pix))
            continue
        end

        % otherwise include if it touches outer
        if any(initialCapture_outer(pix))
            finalCapture_outer(pix) = true;
        end
    end
    finalCapture_outer = bwareaopen(finalCapture_outer, min_keep_pixels);

    % OUTER resorption
    initialCapture_outer_R = Data_Resorption_bin & OP_dil;
    CC_R_outer = bwconncomp(Data_Resorption_bin);
    finalCapture_outer_R = false(size(Data_Resorption_bin));

    for k = 1:CC_R_outer.NumObjects
        pix = CC_R_outer.PixelIdxList{k};

        % SKIP if already counted in INNER
        if any(INNER_assigned_mask(pix))
            continue
        end

        if any(initialCapture_outer_R(pix))
            finalCapture_outer_R(pix) = true;
        end
    end
    finalCapture_outer_R = bwareaopen(finalCapture_outer_R, min_keep_pixels);

    % Save outer masks
    Outer_Formation(:,:,i)  = finalCapture_outer;
    Outer_Resorption(:,:,i) = finalCapture_outer_R;


    % ===============================
    %  3) ---- METRICS
    %  ===============================
    j = j + 1;
    sum_pix_formation_inner(j)   = sum(finalCapture_inner(:));
    sum_pix_formation_outer(j)   = sum(finalCapture_outer(:));
    sum_pix_resorption_inner(j)  = sum(finalCapture_inner_R(:));
    sum_pix_resorption_outer(j)  = sum(finalCapture_outer_R(:));
    sum_pix_prebone(j)           = sum(PreBone_nofibend(:,:,i), "all") / 255;

end


% Plot 
x=linspace(1,stop,stop);
fig1=figure(1);
hold on 
plot(sum_pix_formation_outer,x,'b',LineWidth=2);
plot(sum_pix_formation_inner,x,'C',LineWidth=2);
ylabel('Slice number (0 <- Distal     Proximal -> 100)');
xlabel('Number of pixel per slice');
legend('Periosteum', 'Endosteum'); 
title('Formation - Tibia distal end');

fig2=figure(2);
hold on 
plot(sum_pix_resorption_outer,x,'r',LineWidth=2);
plot(sum_pix_resorption_inner,x,'m',LineWidth=2);
ylabel('Slice number (0 <- Distal     Proximal -> 100)');
xlabel('Number of pixel per slice');
legend('Periosteum', 'Endosteum'); 
title('Resorption - Tibia distal end');


% fig3=figure(3);
% imshow(Data_WholeBone_nofibend(:,:,5));
% 
% fig4=figure(4);
% imshow(Data_WholeBone_nofibend(:,:,15));
% 
% fig5=figure(5);
% imshow(Data_WholeBone_nofibend(:,:,25));

fig6=figure(6);
plot(Inner_perimeter_length_um,x);
ylabel('Slice number (0 <- Distal     Proximal -> 100)');
xlabel('Endosteal Perimeter length (um)'); 
title('Endosteal Perimeter length ');
xlim([0, max(Inner_perimeter_length_um)+500]);

fig7=figure(7);
plot(Outer_perimeter_length_um,x);
ylabel('Slice number (0 <- Distal     Proximal -> 100)');
xlabel('Periosteal Perimeter length (um)'); 
title(' Periosteal Perimeter length ');
xlim([0, max(Outer_perimeter_length_um+500)]);



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
for i=start:stop
    if Prox==1 %  if proximal end of the tibia : remove fibula from wholeBone data set
        WB_filled=imfill(Outer_perim_dilated(:,:,i));
        WB_noFib=WB_filled & Data_WholeBone(:,:,i);
        WB_PreBone_noFib(:,:,i)=WB_filled & PreBone(:,:,i);
        % cortical_3d(:,:,i)=WB_noFib;
        cortical_3d(:,:,i)=WB_PreBone_noFib(:,:,i);
        if Trab_only==1 % trabecular bone comportement isolation
                se_test=strel('Disk',8);
                Inner_perim_close{i}=imclose(Inner_perim(:,:,i),se_test);
                Inner_perim_close_fill{i}=imfill(Inner_perim_close{i},'holes');
                cortical{i}=I_fill{i}-Inner_perim_close_fill{i};
                cortical_bw{i}=imbinarize(cortical{i});
                I_nofib{i}=I{i} & I_fill {i};
                trab{i}=I_nofib{i}-cortical{i};
                trab_bw{i}=imbinarize(trab{i});
                trab_area{i}=bwarea(trab_bw{i});
                trab_3d(:,:,i)=trab_bw{i};            
        end 
        
    end
    if Mid==1
        % cortical_3d(:,:,i)=Data_WholeBone(:,:,i)/255;
        cortical_3d(:,:,i)=PreBone_nofibend(:,:,i);
    end
     if Distal==1
        % cortical_3d(:,:,i)=Data_WholeBone(:,:,i)/255;
        cortical_3d(:,:,i)=PreBone_nofibend(:,:,i);
    end
end

if Trab_only==1 % if trab segmentation was needed -> check resulst
im_Check=100;
figure(8)
trab_overlay=imoverlay(Data_WholeBone(:,:,im_Check),trab_bw{im_Check},'red');
imshow(trab_overlay)
title('Trabecular bone segmentation (red)')
end 


%-------------------------------
% AUTOMATIC ENDO / PERIO / BOTH
%-------------------------------

% Modes definition: {ModeName, Endo_only, Perio_only, Endo_Perio}
modes = {
    'Endo',  1, 0, 0
    'Perio', 0, 1, 0
    'EndoPerio',  0, 0, 1};

se2 = strel('Disk',2); % structuring element for dilation
se3 = strel('Disk',3); % structuring element for dilation

% -------------------------------
% STORE RESULTS PER MODE (so nothing gets overwritten)
% -------------------------------
results = struct();
results(1).modeName = 'Endo';
results(2).modeName = 'Perio';
results(3).modeName = 'EndoPerio';


for m = 1:size(modes,1)
    Endo_only  = modes{m,2};
    Perio_only = modes{m,3};
    Endo_Perio = modes{m,4};
    modeName   = modes{m,1};

    fprintf('\n==== Running mode: %s (Sample %s) ====\n', modeName, Folder);
   
    Outer_percent_forming_surf_px = nan(1, stop);
    Outer_percent_Resor_surf_px   = nan(1, stop);

    Inner_percent_forming_surf_px = nan(1, stop);
    Inner_percent_Resor_surf_px   = nan(1, stop);

    all_percent_forming_surf_px   = nan(1, stop);
    all_percent_Resor_surf_px     = nan(1, stop);

    % -------------------------------
    % Initialize masks
    % -------------------------------
    Formation_Cort_3d  = false(size(cortical_3d));
    Resorption_Cort_3d = false(size(cortical_3d));
    
    Formation_dilated   = false(size(cortical_3d));
    Resorption_dilated  = false(size(cortical_3d));
    
    contact_InnerPerim_Form = false(size(cortical_3d));
    contact_InnerPerim_Resor = false(size(cortical_3d));
    contact_OuterPerim_Form = false(size(cortical_3d));
    contact_OuterPerim_Resor = false(size(cortical_3d));
    contact_allPerim_Form = false(size(cortical_3d));
    contact_allPerim_Resor = false(size(cortical_3d));
    
    forming_inner_perim_px = nan(size(total_inner_perim_px));
    Resor_inner_perim_px   = nan(size(total_inner_perim_px));
    forming_Outer_perim_px = nan(size(total_outer_perim_px));
    Resor_Outer_perim_px   = nan(size(total_outer_perim_px));
    forming_all_perim_px   = nan(size(total_all_perim_px));
    Resor_all_perim_px     = nan(size(total_all_perim_px));

    % -------------------------------
    % Create masks (keep _bw for QC / later use)
    % -------------------------------
    for i = start:stop
        if Endo_only
            Data_Resorption_bw{i} = cortical_3d(:,:,i) & Inner_Resorption(:,:,i);
            Resorption_Cort_3d(:,:,i) = bwmorph(Inner_Resorption(:,:,i),'clean');
            Data_Formation_bw{i}   = cortical_3d(:,:,i) & Inner_Formation(:,:,i);
            Formation_Cort_3d(:,:,i) = bwmorph(Inner_Formation(:,:,i),'clean');

        elseif Perio_only
            Data_Resorption_bw{i} = cortical_3d(:,:,i) & Outer_Resorption(:,:,i);
            Resorption_Cort_3d(:,:,i) = bwmorph(Outer_Resorption(:,:,i),'clean');
            Data_Formation_bw{i}   = cortical_3d(:,:,i) & Outer_Formation(:,:,i);
            Formation_Cort_3d(:,:,i) = bwmorph(Outer_Formation(:,:,i),'clean');

        elseif Endo_Perio
            Data_Resorption_bw{i} = cortical_3d(:,:,i) & (Outer_Resorption(:,:,i) | Inner_Resorption(:,:,i));
            Resorption_Cort_3d(:,:,i) = Outer_Resorption(:,:,i) | Inner_Resorption(:,:,i);
            Data_Formation_bw{i}   = cortical_3d(:,:,i) & (Outer_Formation(:,:,i) | Inner_Formation(:,:,i));
            Formation_Cort_3d(:,:,i) = Outer_Formation(:,:,i) | Inner_Formation(:,:,i);
        end
    end

    % -------------------------------
    % QC visualization
    % -------------------------------
    s = 50; if Trab_only==1, s=100; end
    
    if Endo_only
        F_bin = Formation_Cort_3d(:,:,s); R_bin = Resorption_Cort_3d(:,:,s); modeStr = 'Endosteal (Endo)';
    elseif Perio_only
        F_bin = Formation_Cort_3d(:,:,s); R_bin = Resorption_Cort_3d(:,:,s); modeStr = 'Periosteal (Perio)';
    else
        F_bin = Formation_Cort_3d(:,:,s); R_bin = Resorption_Cort_3d(:,:,s); modeStr = 'Endo+Perio (Both)';
    end

    % Formation QC overlay
    F_orig_bin = imbinarize(Data_Formation(:,:,s));
    F_captured = F_orig_bin & F_bin;
    F_missed   = F_orig_bin & ~F_bin;
    F_added    = ~F_orig_bin & F_bin;
    RGB_F = zeros([size(F_orig_bin),3]);
    RGB_F(:,:,1) = F_missed; RGB_F(:,:,2) = F_captured; RGB_F(:,:,3) = F_added;
    figure; imshow(RGB_F); title(['Formation QC: ' modeStr ' - Green: Included for analysis; Red : Excluded']);
    % figure; imshow(F_orig_bin); hold on; contour(F_bin,[0.5 0.5],'y','LineWidth',1.5); title(['Formation Contour: ' modeStr]);

    % Resorption QC overlay
    R_orig_bin = imbinarize(Data_Resorption(:,:,s));
    R_captured = R_orig_bin & R_bin;
    R_missed   = R_orig_bin & ~R_bin;
    R_added    = ~R_orig_bin & R_bin;
    RGB_R = zeros([size(R_orig_bin),3]);
    RGB_R(:,:,1) = R_missed; RGB_R(:,:,2) = R_captured; RGB_R(:,:,3) = R_added;
    figure; imshow(RGB_R); title(['Resorption QC: ' modeStr ' - Green: Included for analysis; Red : Excluded']);
    % figure; imshow(R_orig_bin); hold on; contour(R_bin,[0.5 0.5],'m','LineWidth',1.5); title(['Resorption Contour: ' modeStr]);

    % -------------------------------
    % Overlay: Prebone - Formation - Resorption
    % -------------------------------
    s2 = 20; if Prox==1, s2=100; end
    slice1 = double(cortical_3d(:,:,s2));
    slice_formation = double(Formation_Cort_3d(:,:,s2));
    slice_resorption = double(Resorption_Cort_3d(:,:,s2));
    background_only = double(slice1 & ~slice_formation & ~slice_resorption);

    overlay1 = cat(3,0.8*background_only + slice_resorption, 0.8*background_only, 0.8*background_only + slice_resorption);
    overlay1 = min(overlay1,1); figure; imshow(overlay1); title([modeStr ': Resorption only (magenta)' ]);
    overlay2 = cat(3,0.8*background_only, 0.8*background_only + slice_formation, 0.8*background_only + slice_formation);
    overlay2 = min(overlay2,1); figure; imshow(overlay2); title([modeStr ': Formation only (cyan)']);
    overlay3 = cat(3,0.8*background_only + slice_resorption, 0.8*background_only + slice_formation, 0.8*background_only + slice_formation + slice_resorption);
    overlay3 = min(overlay3,1); figure; imshow(overlay3); title([modeStr ': Formation (cyan) & Resorption (magenta)']);

    % -------------------------------
    % MS / ES calculation (normalized by perimeter)
    % -------------------------------
    %Preallocate (recommended)
Inner_percent_forming_surf_px = nan(1, size(Inner_perim,3));
Inner_percent_Resor_surf_px   = nan(1, size(Inner_perim,3));
Outer_percent_forming_surf_px = nan(1, size(Outer_perim,3));
Outer_percent_Resor_surf_px   = nan(1, size(Outer_perim,3));
all_percent_forming_surf_px   = nan(1, size(Outer_perim,3));
all_percent_Resor_surf_px     = nan(1, size(Outer_perim,3));

if Endo_only
    for i = start:stop
        % ensure logical
        Inner_perim(:,:,i) = logical(Inner_perim(:,:,i));

        Formation_dilated(:,:,i) = imdilate(logical(Formation_Cort_3d(:,:,i)), se_3_sqr);
        Resorption_dilated(:,:,i)= imdilate(logical(Resorption_Cort_3d(:,:,i)), se_3_sqr);

        % contacts
        contact_InnerPerim_Form(:,:,i)  = Inner_perim(:,:,i) & Formation_dilated(:,:,i);
        contact_InnerPerim_Resor(:,:,i) = Inner_perim(:,:,i) & Resorption_dilated(:,:,i);

        % PIXEL perimeter denominator
        den = nnz(Inner_perim(:,:,i));
        if den > 0
            Inner_percent_forming_surf_px(i) = 100 * nnz(contact_InnerPerim_Form(:,:,i))  / den;
            Inner_percent_Resor_surf_px(i)   = 100 * nnz(contact_InnerPerim_Resor(:,:,i)) / den;
        end
    end

    nVox_Formation_endo = sum(Inner_Formation(:),'all');
    FormationVolume_um3_endo = nVox_Formation_endo * voxelVolume_um3;
    nVox_Resorption_endo = sum(Inner_Resorption(:),'all');
    ResorptionVolume_um3_endo = nVox_Resorption_endo * voxelVolume_um3;
    PreBone_BV=(sum(cortical_3d,"all"))*voxelVolume_um3;

    MS_avg_Innerperim  = mean(Inner_percent_forming_surf_px(start:stop), 'omitnan'); %Endosteal mineralizing surface
    ES_avg_Innerperim  = mean(Inner_percent_Resor_surf_px(start:stop),   'omitnan'); %Endosteal eroding surface
    BFR_avg_Innerperim=100*FormationVolume_um3_endo/(days*PreBone_BV); % formed bone volume on the endosteum/ total bone volume /day (BFR.BV)
    BRR_avg_Innerperim=100*ResorptionVolume_um3_endo/(days*PreBone_BV); % formed bone volume on the endosteum/ total bone volume /day (BFR.BV)
    BFR_BS_endo = FormationVolume_um3_endo / (days * S_endo_um2);
    BRR_BS_endo = ResorptionVolume_um3_endo / (days * S_endo_um2);
    
    %show result in the command window for manual recording
    fprintf('\nResults - Endosteal Surface\n');
    fprintf('ENDO.MS = %.4f (%%)\n', MS_avg_Innerperim);
    fprintf('ENDO.ES = %.4f (%%)\n', ES_avg_Innerperim);
    fprintf('ENDO.BFR/BV = %.4f (%%/day)\n', BFR_avg_Innerperim);
    fprintf('ENDO.BRR/BV = %.4f (%%/day)\n', BRR_avg_Innerperim);
    fprintf('ENDO.BFR/BS = %.4f (um3/um2/d)\n', BFR_BS_endo);
    fprintf('ENDO.BRR/BS = %.4f (um3/um2/d)\n', BRR_BS_endo);
end

if Perio_only
    for i = start:stop
        % ensure logical
        Outer_perim(:,:,i) = logical(Outer_perim(:,:,i));

        % Formation_dilated(:,:,i) = imdilate(logical(Formation_Cort_3d(:,:,i)), se_0);
        Formation_dilated(:,:,i) = imdilate(logical(Formation_Cort_3d(:,:,i)),se_3_sqr);
        Resorption_dilated(:,:,i)= imdilate(logical(Resorption_Cort_3d(:,:,i)), se_3_sqr);

        % contacts
        contact_OuterPerim_Form(:,:,i)  = Outer_perim(:,:,i) & Formation_dilated(:,:,i);
        contact_OuterPerim_Resor(:,:,i) = Outer_perim(:,:,i) & Resorption_dilated(:,:,i);

        % PIXEL perimeter denominator
        den = nnz(Outer_perim(:,:,i));
        if den > 0
            Outer_percent_forming_surf_px(i) = 100 * nnz(contact_OuterPerim_Form(:,:,i))  / den;
            Outer_percent_Resor_surf_px(i)   = 100 * nnz(contact_OuterPerim_Resor(:,:,i)) / den;
        end
    end

    nVox_Formation_perio = sum(Outer_Formation(:),'all'); %calculate the of volume of bone formation of the perisoteal surface
    FormationVolume_um3_perio = nVox_Formation_perio * voxelVolume_um3; 
    nVox_Resorption_perio = sum(Outer_Resorption(:),'all');
    ResorptionVolume_um3_perio = nVox_Resorption_perio * voxelVolume_um3;
    PreBone_BV=(sum(cortical_3d,"all"))*voxelVolume_um3;

    MS_avg_Outerperim  = mean(Outer_percent_forming_surf_px(start:stop), 'omitnan');
    ES_avg_Outerperim  = mean(Outer_percent_Resor_surf_px(start:stop),   'omitnan');
    BFR_avg_Outerperim=100*FormationVolume_um3_perio/(days*PreBone_BV); % formed bone volume on the endosteum/ total bone volume /day
    BRR_avg_Outerperim=100*ResorptionVolume_um3_perio/(days*PreBone_BV); % formed bone volume on the endosteum/ total bone volume /day
    BFR_BS_perio = FormationVolume_um3_perio / (days * S_perio_um2);
    BRR_BS_perio = ResorptionVolume_um3_perio / (days * S_perio_um2);

     %show result in the command window for manual recording
    fprintf('\nResults - Periosteal Surface\n');
    fprintf('Perio.MS = %.4f (%%)\n', MS_avg_Outerperim);
    fprintf('Perio.ES = %.4f (%%)\n', ES_avg_Outerperim);
    fprintf('Perio.BFR/BV = %.4f (%%/day)\n', BFR_avg_Outerperim);
    fprintf('Perio.BRR/BV = %.4f (%%/day)\n', BRR_avg_Outerperim);
    fprintf('Perio.BFR/BS = %.4f (um3/um2/d)\n', BFR_BS_perio);
    fprintf('Perio.BRR/BS = %.4f (um3/um2/d)\n', BRR_BS_perio);
end

if Endo_Perio
    for i = start:stop
        % ensure logical
        Outer_perim(:,:,i) = logical(Outer_perim(:,:,i));
        Inner_perim(:,:,i) = logical(Inner_perim(:,:,i));

        Formation_dilated(:,:,i) = imdilate(logical(Formation_Cort_3d(:,:,i)), se_3_sqr);
        Resorption_dilated(:,:,i)= imdilate(logical(Resorption_Cort_3d(:,:,i)), se_3_sqr);

        all_perim(:,:,i) = Outer_perim(:,:,i) | Inner_perim(:,:,i);

        % contacts
        contact_allPerim_Form(:,:,i)  = all_perim(:,:,i) & Formation_dilated(:,:,i);
        contact_allPerim_Resor(:,:,i) = all_perim(:,:,i) & Resorption_dilated(:,:,i);

        % PIXEL perimeter denominator
        den = nnz(all_perim(:,:,i));
        if den > 0
            all_percent_forming_surf_px(i) = 100 * nnz(contact_allPerim_Form(:,:,i))  / den;
            all_percent_Resor_surf_px(i)   = 100 * nnz(contact_allPerim_Resor(:,:,i)) / den;
        end
    end

    nVox_Formation_EndoPerio = sum(Formation_Cort_3d(:),'all');
    FormationVolume_um3_EndoPerio = nVox_Formation_EndoPerio * voxelVolume_um3;
    nVox_Resorption_EndoPerio = sum(Resorption_Cort_3d(:),'all');
    ResorptionVolume_um3_EndoPerio = nVox_Resorption_EndoPerio * voxelVolume_um3;
    PreBone_BV=(sum(cortical_3d,"all"))*voxelVolume_um3;

    MS_avg_allperim  = mean(all_percent_forming_surf_px(start:stop), 'omitnan');
    ES_avg_allperim  = mean(all_percent_Resor_surf_px(start:stop),   'omitnan');
    BFR_avg_allperim=100*FormationVolume_um3_EndoPerio/(days*PreBone_BV); % formed bone volume on the endosteum/ total bone volume /day
    BRR_avg_allperim=100*ResorptionVolume_um3_EndoPerio/(days*PreBone_BV); % formed bone volume on the endosteum/ total bone volume /day
    FormationVolume_um3_endo  = sum(Inner_Formation(:),'all')  * voxelVolume_um3;
    ResorptionVolume_um3_endo = sum(Inner_Resorption(:),'all') * voxelVolume_um3;
    FormationVolume_um3_perio  = sum(Outer_Formation(:),'all')  * voxelVolume_um3;
    ResorptionVolume_um3_perio = sum(Outer_Resorption(:),'all') * voxelVolume_um3;

    BFR_BS_endo  = FormationVolume_um3_endo  / (days * S_endo_um2);
    BRR_BS_endo  = ResorptionVolume_um3_endo / (days * S_endo_um2);
    BFR_BS_perio = FormationVolume_um3_perio / (days * S_perio_um2);
    BRR_BS_perio = ResorptionVolume_um3_perio / (days * S_perio_um2);

    %show result in the command window for manual recording
    fprintf('\nResults - Endosteal + Perisoteal Surface\n');
    fprintf('EndoPerio.MS = %.4f (%%)\n', MS_avg_allperim);
    fprintf('EndoPerio.ES = %.4f (%%)\n', ES_avg_allperim);
    fprintf('EndoPerio.BFR/BV = %.4f (%%/day)\n', BFR_avg_allperim);
    fprintf('EndoPerio.BRR/BV = %.4f (%%/day)\n', BRR_avg_allperim);
    fprintf('EndoPerio.BFR/BS = %.4f (um3/um2/d)\n', BFR_BS_perio+BFR_BS_endo);
    fprintf('EndoPerio.BRR/BS = %.4f (um3/um2/d)\n', BRR_BS_perio+BRR_BS_endo);

end
    % -------------------------------
    % SAVE EVERYTHING FOR THIS MODE
    % -------------------------------
    results(m).Endo_only  = Endo_only;
    results(m).Perio_only = Perio_only;
    results(m).Endo_Perio = Endo_Perio;
    results(m).S_endo_um2  = S_endo_um2;
    results(m).S_perio_um2 = S_perio_um2;

    % Per-slice percentages
    results(m).Outer_percent_forming_surf_px = Outer_percent_forming_surf_px;
    results(m).Outer_percent_Resor_surf_px   = Outer_percent_Resor_surf_px;
    
    results(m).Inner_percent_forming_surf_px = Inner_percent_forming_surf_px;
    results(m).Inner_percent_Resor_surf_px   = Inner_percent_Resor_surf_px;
    
    results(m).all_percent_forming_surf_px   = all_percent_forming_surf_px;
    results(m).all_percent_Resor_surf_px     = all_percent_Resor_surf_px;
    
    % Per-slice contact pixel counts
    results(m).forming_inner_perim_px = forming_inner_perim_px;
    results(m).Resor_inner_perim_px   = Resor_inner_perim_px;
    
    results(m).forming_Outer_perim_px = forming_Outer_perim_px;
    results(m).Resor_Outer_perim_px   = Resor_Outer_perim_px;
    
    results(m).forming_all_perim_px   = forming_all_perim_px;
    results(m).Resor_all_perim_px     = Resor_all_perim_px;
    
    % Save MS/ES/BFR/BRR depending on mode
    if Endo_only
        results(m).MS  = MS_avg_Innerperim;
        results(m).ES  = ES_avg_Innerperim;
        results(m).BFR = BFR_avg_Innerperim;
        results(m).BRR = BRR_avg_Innerperim;
        results(m).BFR_BS_endo = BFR_BS_endo;
        results(m).BRR_BS_endo = BRR_BS_endo;
    elseif Perio_only
        results(m).MS  = MS_avg_Outerperim;
        results(m).ES  = ES_avg_Outerperim;
        results(m).BFR = BFR_avg_Outerperim;
        results(m).BRR = BRR_avg_Outerperim;
        results(m).BFR_BS_perio = BFR_BS_perio;
        results(m).BRR_BS_perio = BRR_BS_perio;
    elseif Endo_Perio
        results(m).MS  = MS_avg_allperim;
        results(m).ES  = ES_avg_allperim;
        results(m).BFR = BFR_avg_allperim;
        results(m).BRR = BRR_avg_allperim;
        results(m).BFR_BS_endo  = BFR_BS_endo;
        results(m).BRR_BS_endo  = BRR_BS_endo;
        results(m).BFR_BS_perio = BFR_BS_perio;
        results(m).BRR_BS_perio = BRR_BS_perio;
    end
    
    % (Optional) store masks for later QC / debugging
    results(m).Formation_Cort_3d  = Formation_Cort_3d;
    results(m).Resorption_Cort_3d = Resorption_Cort_3d;
    
    results(m).contact_InnerPerim_Form = contact_InnerPerim_Form;
    results(m).contact_InnerPerim_Resor = contact_InnerPerim_Resor;
    results(m).contact_OuterPerim_Form = contact_OuterPerim_Form;
    results(m).contact_OuterPerim_Resor = contact_OuterPerim_Resor;
    results(m).contact_allPerim_Form   = contact_allPerim_Form;
    results(m).contact_allPerim_Resor  = contact_allPerim_Resor;



    % -------------------------------
    % Export metrics to Excel (safe copy)
    % -------------------------------
    Cort_excel = directory_excelfile;
    local_copy = fullfile(tempdir, 'results_3DHisto_local.xlsx');

    system('taskkill /F /IM EXCEL.EXE'); pause(0.5);
    copyfile(Cort_excel, local_copy, 'f');

    sample_num = regexp(Folder, '^\d+', 'match'); sample_num = string(sample_num{1});
    listSheet = "List_samples_groups";

    try
        group_table_raw = readcell(local_copy, 'Sheet', listSheet);
    catch
        headers = {'Group','SampleID'}; writecell(headers, local_copy, 'Sheet', listSheet, 'UseExcel', false);
        group_table_raw = readcell(local_copy, 'Sheet', listSheet);
    end

    all_groups  = string(group_table_raw(2:end,1));
    all_samples = string(group_table_raw(2:end,2));
    idx = find(all_samples == sample_num);
    if isempty(idx), error("Sample %s not found in List_samples_groups!", sample_num); end
    group_name = all_groups(idx);

    sum_F = sum(Formation_Cort_3d,"all"); sum_R = sum(Resorption_Cort_3d,"all"); sum_PreBone = sum(cortical_3d,"all");
    F_BV = sum_F/sum_PreBone; R_BV = sum_R/sum_PreBone;

    % Choose sheet & measurement row based on flags
    if Prox==1 && Trab_only==1
        sheet = "Proxi_TrabOnly"; measure_row = {MS_avg_Innerperim, ES_avg_Innerperim, BFR_avg_Innerperim, BRR_avg_Innerperim, BFR_BS_endo, BRR_BS_endo};
    elseif Prox==1 && Perio_only==1 
        sheet = "Proxi_Perio"; measure_row = {MS_avg_Outerperim, ES_avg_Outerperim, BFR_avg_Outerperim, BRR_avg_Outerperim, BFR_BS_perio, BRR_BS_perio};
    elseif Prox==1 && Endo_only==1 
        sheet = "Proxi_Endo_CortTrab"; measure_row = {MS_avg_Innerperim, ES_avg_Innerperim, BFR_avg_Innerperim, BRR_avg_Innerperim, BFR_BS_endo, BRR_BS_endo};
    elseif Prox==1 && Endo_Perio==1 
        sheet = "Proxi_EndoPerio"; measure_row = {MS_avg_allperim, ES_avg_allperim, BFR_avg_allperim, BRR_avg_allperim,BFR_BS_perio, BRR_BS_perio, BFR_BS_endo, BRR_BS_endo};
    elseif Mid==1 && Endo_only==1 && nowing==0
        sheet = "Mid_Endo"; measure_row = {MS_avg_Innerperim, ES_avg_Innerperim, BFR_avg_Innerperim, BRR_avg_Innerperim, BFR_BS_endo, BRR_BS_endo};
    elseif Mid==1 && Perio_only==1 && nowing==0
        sheet = "Mid_Perio"; measure_row = {MS_avg_Outerperim, ES_avg_Outerperim, BFR_avg_Outerperim, BRR_avg_Outerperim, BFR_BS_perio, BRR_BS_perio};
    elseif Mid==1 && Endo_Perio==1 && nowing==0
        sheet = "Mid_EndoPerio"; measure_row = {MS_avg_allperim, ES_avg_allperim, BFR_avg_allperim, BRR_avg_allperim,BFR_BS_perio, BRR_BS_perio, BFR_BS_endo, BRR_BS_endo};
    elseif Mid==1 && Perio_only==1 && nowing==1
        sheet = "Mid_Perio_NoWing"; measure_row = {MS_avg_Outerperim, ES_avg_Outerperim, BFR_avg_Outerperim, BRR_avg_Outerperim, BFR_BS_perio, BRR_BS_perio};
    elseif Mid==1 && Endo_only==1 && nowing==1
        sheet = "Mid_Endo_NoWing"; measure_row = {MS_avg_Innerperim, ES_avg_Innerperim, BFR_avg_Innerperim, BRR_avg_Innerperim, BFR_BS_endo, BRR_BS_endo};
    elseif Mid==1 && Endo_Perio==1 && nowing==1
        sheet = "Mid_EndoPerio_NoWing"; measure_row = {MS_avg_allperim, ES_avg_allperim, BFR_avg_allperim, BRR_avg_allperim, BFR_BS_perio, BRR_BS_perio, BFR_BS_endo, BRR_BS_endo};
     elseif Distal==1 && Endo_only==1 && nowing==0
        sheet = "Distal_Endo"; measure_row = {MS_avg_Innerperim, ES_avg_Innerperim, BFR_avg_Innerperim, BRR_avg_Innerperim, BFR_BS_endo, BRR_BS_endo };
    elseif Distal==1 && Perio_only==1 && nowing==0
        sheet = "Distal_Perio"; measure_row = {MS_avg_Outerperim, ES_avg_Outerperim, BFR_avg_Outerperim, BRR_avg_Outerperim, BFR_BS_perio, BRR_BS_perio};
    elseif Distal==1 && Endo_Perio==1 && nowing==0
        sheet = "Distal_EndoPerio"; measure_row = {MS_avg_allperim, ES_avg_allperim, BFR_avg_allperim, BRR_avg_allperim, BFR_BS_perio, BRR_BS_perio, BFR_BS_endo, BRR_BS_endo};
    else
        error("Unknown combination of flags.");
    end

     % defaults (avoid "undefined variable" depending on mode)
    if ~exist('BFR_BS_perio','var'), BFR_BS_perio = NaN; end
    if ~exist('BRR_BS_perio','var'), BRR_BS_perio = NaN; end
    if ~exist('BFR_BS_endo','var'),  BFR_BS_endo  = NaN; end
    if ~exist('BRR_BS_endo','var'),  BRR_BS_endo  = NaN; end
    
    new_row = {group_name, sample_num, sum_R, sum_F, sum_PreBone, F_BV, R_BV, measure_row{:}};

    % new_row = {group_name, sample_num, sum_R, sum_F, sum_PreBone, F_BV, R_BV, measure_row{:}};

    try
        raw = readcell(local_copy, 'Sheet', sheet);
    catch
        headers = {'Group','SampleID','Resorption','Formation','PreBone','F/BV','R/BV', ...
                   'MS','ES','BFR','BRR','BFR_BS','BRR_BS'};
        writecell(headers, local_copy, 'Sheet', sheet, 'UseExcel', false);
        raw = readcell(local_copy, 'Sheet', sheet);
    end
    headers = raw(1,:); data = raw(2:end,:);
    existing_sample_ids = string(data(:,2)); match_idx = find(existing_sample_ids == sample_num);
    if isempty(match_idx)
        data = [data; new_row]; fprintf('Added NEW sample %s to sheet %s\n', sample_num, sheet);
    else
        data(match_idx,:) = new_row; fprintf('Updated sample %s in sheet %s\n', sample_num, sheet);
    end

    writecell([headers; data], local_copy, 'Sheet', sheet, 'UseExcel', false);
    copyfile(local_copy, Cort_excel, 'f'); fprintf('✓ Excel file updated safely to Box without locks.\n');
    system('taskkill /F /IM EXCEL.EXE');
end



%%
    % % -------------------------------
    % % 3D Volume visualization
    % % -------------------------------
    % out = cortical_3d;
    % In_F = Formation_Cort_3d;
    % In_R = Resorption_Cort_3d;
    % 
    % titleText = "3D rendering - " + modeStr + " - Formation (cyan) & Resorption (magenta) ";
    % viewerLabels2 = viewer3d(BackgroundColor="white",BackgroundGradient="off",CameraZoom=2);
    % uilabel(viewerLabels2.Parent, ...
    % 'Text',titleText, ...
    % 'FontSize',16, ...
    % 'FontWeight','bold', ...
    % 'HorizontalAlignment','center', ...
    % 'Position',[20 viewerLabels2.Parent.Position(4)-40 ...
    %             viewerLabels2.Parent.Position(3)-40 30]);
    % 
    % volshow(out,Parent=viewerLabels2, RenderingStyle="GradientOpacity", ...
    %     Alphamap=linspace(0,0.3,256).^1.2, Colormap=repmat(linspace(0,1,256)',1,3), ...
    %     OverlayData=In_F, OverlayAlpha=0.2, OverlayColormap=repmat([0 1 1],256,1));
    % 
    % volshow(out,Parent=viewerLabels2, RenderingStyle="GradientOpacity", ...
    %     Alphamap=linspace(0,0.3,256).^1.2, Colormap=repmat(linspace(0,1,256)',1,3), ...
    %     OverlayData=In_R, OverlayAlpha=0.2, OverlayColormap=repmat([1 0 1],256,1));

    out = cortical_3d;
    In_F = Formation_Cort_3d;
    In_R = Resorption_Cort_3d;

    viewerLabels2 = viewer3d(BackgroundColor="white",BackgroundGradient="off",CameraZoom=2);

% main greyscale bone volume (no overlay alpha needed)
hBone = safeVolshow(viewerLabels2, out, ...
    'RenderingStyle','GradientOpacity', ...
    'Alphamap',linspace(0,0.3,256).^1.2, ...
    'Colormap',repmat(linspace(0,1,256)',1,3));

% formation overlay (cyan)
hForm = safeVolshow(viewerLabels2, out, ...
    'RenderingStyle','GradientOpacity', ...
    'Alphamap',linspace(0,0.3,256).^1.2, ...
    'Colormap',repmat(linspace(0,1,256)',1,3), ...
    'OverlayData', In_F, ...
    'OverlayColormap', repmat([0 1 1],256,1), ...
    'OverlayAlpha', 0.2);

% resorption overlay (magenta)
hRes = safeVolshow(viewerLabels2, out, ...
    'RenderingStyle','GradientOpacity', ...
    'Alphamap',linspace(0,0.3,256).^1.2, ...
    'Colormap',repmat(linspace(0,1,256)',1,3), ...
    'OverlayData', In_R, ...
    'OverlayColormap', repmat([1 0 1],256,1), ...
    'OverlayAlpha', 0.2);

   
%%
%%
i = 38;   % slice index

Surface = 'Perio';   % 'Endo' or 'Perio'
Mask    = 'F';      % 'F' = Formation | 'R' = Resorption

if strcmpi(Surface,'Endo')

    perim = logical(Inner_perim(:,:,i));

    if strcmpi(Mask,'F')
        mask_orig = logical(Inner_Formation(:,:,i));
        contact   = logical(results(1).contact_InnerPerim_Form(:,:,i));
        maskName  = 'Formation';
    elseif strcmpi(Mask,'R')
        mask_orig = logical(Inner_Resorption(:,:,i));
        contact   = logical(results(1).contact_InnerPerim_Resor(:,:,i));
        maskName  = 'Resorption';
    else
        error('Mask must be ''F'' or ''R''.');
    end

    perimName = 'Inner perim';

elseif strcmpi(Surface,'Perio')

    perim = logical(Outer_perim(:,:,i));

    if strcmpi(Mask,'F')
        mask_orig = logical(Outer_Formation(:,:,i));
        contact   = logical(results(2).contact_OuterPerim_Form(:,:,i));
        maskName  = 'Formation';
    elseif strcmpi(Mask,'R')
        mask_orig = logical(Outer_Resorption(:,:,i));
        contact   = logical(results(2).contact_OuterPerim_Resor(:,:,i));
        maskName  = 'Resorption';
    else
        error('Mask must be ''F'' or ''R''.');
    end

    perimName = 'Outer perim';

else
    error('Surface must be ''Endo'' or ''Perio''.');
end

% Initialize RGB
RGB = zeros([size(perim) 3]);

% -------------------------
% Formation / Resorption mask: WHITE
% -------------------------
RGB(:,:,1) = mask_orig;
RGB(:,:,2) = mask_orig;
RGB(:,:,3) = mask_orig;

% -------------------------
% Perimeter: RED
% -------------------------
RGB(:,:,1) = RGB(:,:,1) | perim;

% -------------------------
% Contact: GREEN (override)
% -------------------------
RGB(:,:,2) = RGB(:,:,2) | contact;   % ✅ add green, don't overwrite
RGB(:,:,1) = RGB(:,:,1) & ~contact;  % remove red under contact
RGB(:,:,3) = RGB(:,:,3) & ~contact;  % remove blue under contact


% Display
figure;
imshow(RGB);
title(sprintf('%s (red) | %s (white) | Contact (green) – slice %d', ...
    perimName, maskName, i));



%% 
function S_um2 = surfaceArea_um2_fromMask(BW, sx, sy, sz)
    BW = logical(BW);
    if nnz(BW) == 0
        S_um2 = NaN;
        warning('surfaceArea_um2_fromMask: mask is empty -> returning NaN');
        return;
    end

    [F,V] = isosurface(BW, 0.5);

    % scale vertices into real units (µm)
    V(:,1) = V(:,1) * sx;
    V(:,2) = V(:,2) * sy;
    V(:,3) = V(:,3) * sz;

    % surface area (µm^2)
    p1 = V(F(:,1),:);
    p2 = V(F(:,2),:);
    p3 = V(F(:,3),:);
    S_um2 = 0.5 * sum(vecnorm(cross(p2-p1, p3-p1, 2), 2, 2));
end


 function hVol = safeVolshow(viewerParent, V, varargin)
% safeVolshow: wrapper around volshow that sets overlay colormap/alpha robustly
% Usage:
%   hVol = safeVolshow(viewerParent, V, 'OverlayData', overlay, ...
%                      'OverlayColormap', cmap, 'OverlayAlpha', 0.2, ...)
%
% Pass the same name-value pairs you would normally pass to volshow.
% If 'OverlayAlpha' is present in varargin, this function will try to
% apply it using a supported property name for the user's MATLAB release.

    % parse inputs quickly
    p = inputParser;
    addRequired(p,'viewerParent');
    addRequired(p,'V');
    parse(p,viewerParent,V);

    % find OverlayAlpha in varargin (case-sensitive)
    overlayAlpha = [];
    idxAlpha = find(strcmp('OverlayAlpha', varargin), 1);
    if ~isempty(idxAlpha)
        overlayAlpha = varargin{idxAlpha+1};
        % remove it from the varargin list so volshow doesn't choke on ambiguous name
        varargin([idxAlpha, idxAlpha+1]) = [];
    end

    % call volshow with remaining args
    try
        hVol = volshow(V, 'Parent', viewerParent, varargin{:});
    catch ME
        % try without 'Parent' if some users' volshow API differs
        try
            hVol = volshow(V, varargin{:});
        catch
            rethrow(ME)
        end
    end

    % if no overlayAlpha requested, return
    if isempty(overlayAlpha)
        return
    end

    % Try to set overlay alpha using supported property names
    % List of possible property names seen across MATLAB versions:
    candidateProps = { ...
        'OverlayAlpha', ...        % exact name you used
        'OverlayAlphaData', ...    % some releases
        'OverlayAlphaMap', ...     % other variants
        'OverlayOpacity', ...      % hypothetical variant
        'OverlayTransparency' ...  % hypothetical variant
        };

    setSuccess = false;
    for i=1:numel(candidateProps)
        prop = candidateProps{i};
        try
            if isprop(hVol, prop)
                % If prop expects vector/array vs scalar: do an assignment attempt
                hVol.(prop) = overlayAlpha;
                setSuccess = true;
                break
            end
        catch
            % ignore and try next
        end
    end

    % Some releases implement overlay alpha on the *Volume* subclass but don't
    % expose isprop() in the usual way — try set() as last resort
    if ~setSuccess
        try
            set(hVol, 'OverlayAlpha', overlayAlpha);
            setSuccess = true;
        catch
            % ignore
        end
    end

    if ~setSuccess
        warning(['Could not set overlay alpha on this MATLAB release. ' ...
                 'Overlay will be shown with default opacity. If you need ' ...
                 'per-overlay transparency, check that your MATLAB release ' ...
                 'supports it or update MATLAB.']);
    end
end
