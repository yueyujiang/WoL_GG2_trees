# WoL_GG2_trees
## 16K WoL trees
1. 16Ktree.incremental.nwk    
**date** (email GG2 followup meeting from Metin): 12/23/2021.    
**description**: This tree with 16263 sequences is created by inserting new sequences on the reference 10K tree. RF distance to the 10K tree is 0.0018 for the common leaves.     
      
2. 16Ktree.updates.nwk.    
**date** (email GG2 followup meeting from Metin): 12/23/2021.    
**description**: This tree with 16059 sequences is inferred using a partial de-novo strategy. RF distance to the 10K tree is .0982 for the common leaves. Qiyun, please use this tree instead of the one I shared yesterday in your analysis.   
       
3. 16k.update.conserve_bl.nwk.          
**description**: This tree using topology from 16Ktree.updates.nwk and reestimate the branch length using "conserved" site selected by ppa_conserv.py (Qiyun) from amino acid sequences. Note that we reomved 11 species (I don't remember what this is...) + (G001405495, G001072395, and G001787865).     
         
4. 16k.update.random_bl.nwk          
**description**: This tree using topology from 16Ktree.updates.nwk and reestimate the branch length using "conserved" site selected by ppa_conserv.py (Qiyun) from amino acid sequences. Note that we reomved 11 species (I don't remember what this is...) + (G001405495, G001072395, and G001787865).        
             
5. 16K_v2.nwk          
**date** (email new 16K tree from Metin): 04/15/2022           
**description**: contamination removed.         
                   
7. udance.updates.attempt3.nwk            
**date** (email new 16K tree from Metin): 04/20/2022                 
**description**: Degree-2 node problem solved.           
                   
8. 16k_v1_without_14_seqs_decont_supported.nwk           
**date** (email Re: quick question prune & support from Metin): 05/09/2022            
**description**: v1 tree (minus 214 contaminated sequences detected by GUNC minus 14 taxa we always remove) with ASTRAL support and 16k.update.random_bl.nwk branch length (100x).            
        

## GG2 16S tree        
1. 270K.tar.gz           
**date** (email 270K (and 1.7M) tree is ready from Metin): 02/22/2022                   
**description**: uDance was able to extend the 16K tree to 270K tree using the full 16S alignment. In the attached archive, you will find the 270K taxa tree, 1.7M taxa tree with duplicate records added, deduplication map (in case you need it) and a list of ~2800 sequences that uDance couldn't insert. One note that the backbone species without the 16S gene are not present in these trees.      
                 
2. trees_16S_v2.tar.xz                             
**date** (email new 16K tree from Metin): 04/22/2022                              
**description**: a tree with 267K unique sequences and one with 1.7M sequences including duplicates. contamination removed.         
         
