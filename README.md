# Tool name and creators
```
[*]To get started, use the -h option to see what options are available

                                        
                &&&&&&&&&               
              &&&&     &&&&             
             &&&         &&&            
             &&&         &&&            
           .&&&&&&&&&&&&&&&&&           
           &&&&&&&&&&&&&&&&&&&          
           &&&&&&&    #&&&&&&&          
           &&&&&&&&   &&&&&&&&          
           &&&&&&&&  /&&&&&&&&          
           &&&&&&&&& &&&&&&&&&          
           &&&&&&&&&&&&&&&&&&,     
            &&&&&&&&&&&&&&&&
             &&&&&&&&&&&&&&

    Thank you for installing Virscan-py!

[ 0.0.2, Team HKSD (Hritik, Kshitij, Sayantan, Divya) ]

======================================
Virscan-py is a virus scanning tool.
To see a detailed about, use --about
======================================
```

# File hierarchy
```
┬─[divya at racharch in ~/a/virscan-py]─[G:master]
╰──> λ tree -L 1 .
.
├── config.json
├── core
├── data
├── docs
├── env
├── images
├── LICENSE
├── modules
├── README.md
├── reports
├── requirements
├── setup.py
└── virscan

7 directories, 6 files
```

# Modules
```
[*]Available modules are:
>  analyze_file
>  sigma_analyze
>  file_upload
>  all_behav_rep
```

# Commands
```
./virscan -m sigma_analyze -q 24d004a104d4d54034dbcffc2a4b19a11f39008a575aa614ea04703480b1022c -B
./virscan -m all_behav_rep -q 24d004a104d4d54034dbcffc2a4b19a11f39008a575aa614ea04703480b1022c -B
./virscan -m file_upload -q data/eicarcom2.zip -B
./virscan -m analyze_file -q 24d004a104d4d54034dbcffc2a4b19a11f39008a575aa614ea04703480b1022c -B
```
