# WoL_GG2_trees
## 16K WoL trees
1. 16Ktree.incremental.nwk    
**date** (email GG2 followup meeting from Metin): 12/23/2021.    
**description**: This tree with 16263 sequences is created by inserting new sequences on the reference 10K tree. RF distance to the 10K tree is 0.0018 for the common leaves.     
      
2. 16Ktree.updates.nwk.    
**date** (email GG2 followup meeting from Metin): 12/23/2021.    
**description**: This tree with 16059 sequences is inferred using a partial de-novo strategy. RF distance to the 10K tree is .0982 for the common leaves. 
       
3. 16k.update.conserve_bl.nwk.          
**description**: This tree using topology from 16Ktree.updates.nwk and reestimate the branch length using "conserved" site selected by ppa_conserv.py (Qiyun) from amino acid sequences. Note that we removed 14 species in [removed.txt](removed.txt).
         
4. 16k.update.random_bl.nwk          
**description**: This tree using topology from 16Ktree.updates.nwk and reestimate the branch length using randomly selected site from nucleotide sequences. Note that we removed 14 species in [removed.txt](removed.txt).       
             
5. 16K_v2.nwk          
**date** (email new 16K tree from Metin): 04/15/2022           
**description**: contamination removed.         
                   
6. udance.updates.attempt3.nwk            
**date** (email new 16K tree from Metin): 04/20/2022                 
**description**: Degree-2 node problem solved.           
                   
7. 16k_v1_without_14_seqs_decont_supported.nwk           
**date** (email Re: quick question prune & support from Metin): 05/09/2022            
**description**: v1 tree (minus 214 contaminated sequences detected by GUNC minus 14 taxa we always remove) with ASTRAL support annotations (-t2)  and 16k.update.random_bl.nwk branch length.            
        
8. 16k_v1_without_14_seqs_decont_supported_lpponly.nwk           
**date** (email Re: quick question prune & support from Metin): 05/09/2022            
**description**: The same as 16k_v1_without_14_seqs_decont_supported.nwk except branch labels are simply localPP not all the annotations.          
        
9. 16k_v1_without_14_seqs_decont.nwk         
**date** (email Re: quick question prune & support from Metin): 05/09/2022            
**description**: 16k_v1_without_14_seqs_decont_supported.nwk without internal labels.      
        
10. 16k_v1_without_14_seqs_decont_loof.nwk         
**date** 06-02-2022            
**description**: uDance has a filtering protocol based on leave on out placement. Each species in the backbone is removed and added back to the backbone using APPLES-2. If the taxa moves log2(n) edges or more after placement, it's assumed to be mislocated in the backbone and thus removed. 16k_v1_without_14_seqs_decont.nwk is filtered using this protocol and the number of species decreased by 57. 

11. 06-12-2022-16k-v4-loof-backbonenextiter.rt.nwk
**date** 06-12-2022         
**description**: In the uDance run that created 16k_v1_without_14_seqs_decont.nwk, two phyla Myxococcota and Bdellvibrionata were unplaceable and were removed from the output tree. We did a second iteration with larger cluster diameter and placed them. Next we performed the APPLES-2 based filtering mentioned in the previous article. Finally, we rooted the tree at the MRCA of Bacteria.    
        

12. 06-26-2022-200K-udance-astral-bl-5-17-2-rt.nwk
**date** 06-26-2022        
**description**: Using uDance, we updated 06-12-2022-16k-v4-loof-backbonenextiter.rt.nwk with nearly 184,000 sequences. We did not perform an APPLES-2 based leave one out test at the end but we rooted the tree at the middle of A-B branch and estimated the branch lengths in substitution unit using ASTRAL.    

13. 06-12-2022-16k-v4-loof-backbonenextiter.rt.conserve-bl.nwk   
**date** 07-15-2022             
**description**: Same as 06-12-2022-16k-v4-loof-backbonenextiter.rt.nwk. Use the same sites selected in 16k.update.conserve_bl.nwk to reestimate the branch length.               

## GG2 16S tree        
1. 270K.tar.gz           
**date** (email 270K (and 1.7M) tree is ready from Metin): 02/22/2022                    
**description**: uDance was able to extend the 16K tree to 270K tree using the full 16S alignment. In the attached archive, you will find the 270K taxa tree, 1.7M taxa tree with duplicate records added, deduplication map (in case you need it) and a list of ~2800 sequences that uDance couldn't insert. One note that the backbone species without the 16S gene are not present in these trees.          
                 
2. trees_16S_v2.tar.xz                             
**date** (email new 16K tree from Metin): 04/22/2022                              
**description**: a tree with 267K unique sequences and one with 1.7M sequences including duplicates. contamination removed.     

3. 16k_full_length_placement.jplace.       
**date** (email gg2 placement from Yueyu): 05/28/2022.     
**description**: jplace file with unique full length 16S sequences placed using DEPP and the backbone species copies are manually selected by Metin.   

"I removed all copies with errors larger than or equal to 13 branches in the list of error-per-copy you sent me (leave-out placement error for backbone sequences). This filter removed some of the single-copy species too. So the number of backbone sequences decreased to 12201."           

4. 05-29-22-270K-deppplacement.nwk         
**date** 05-29-22 (email thread: gg2 placement)                   
**description**: We removed 105 backbone species from `16k_v1_without_14_seqs_decont_supported.nwk` based on a DEPP based contamination detection protocol. Then we placed all 270K 16S sequences on this backbone tree using DEPP. Finally, the tree is refined using uDance (uses iqtree2 -fast under the hood).

5. 06-02-22-270K-deppplacement.nwk         
**date** 06-02-22 (email thread: gg2 placement)                   
**description**: Same as 05-29-22-270K-deppplacement.nwk but ignore distances between pair of species whose sequences overlap less than 5%.     

6. 07-17-2022-270K-16kv4-backboneiter-loof-15000-shrunk.nwk    
**date** 07-17-22 (email thread: gg2 placement)                   
**description**: Built using uDance covid-edition. The bacbone is 06-26-2022-200K-udance-astral-bl-5-17-2-rt.nwk. The bacbone is filtered using APPLES-2 (for Myxococcota and Bdellvibrionota) and DEPP. uDance output tree is tree-shrunk. 

## Miscellaneous

1. removed.txt                              
**date** (email potential erroneous placements in 16k tree): 01/25/2022

**description**: list of 14 sequences removed from 16k tree. uDance has a backbone filtering mechanism. These 14 are the once that were removed from the backbone once we went from 10K to 16K (incremental + updates combined).        

2. nw_stats.txt                              
**description**: Basic statistics for each newick file.

3. 05-29-22-270K-falsepositives-rt.txt
**description**: Sequences in `05-29-22-270K-deppplacement.nwk` whose taxonomy may be disagreeing with LTP annotation in phylum level.
