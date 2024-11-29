# raspberry-pi-ollama

## Install Ollama
Use the command below to install Ollama CLI:
```{bash}
curl https://ollama.ai/install.sh | sh
```
Use the command below to install Ollama Python Package:
```{bash}
git clone https://github.com/ollama/ollama-python
cd ollama-python
pip install .
```

## Small(er) Models
0. Llama 3.2 Family - ***OPTIMAL***
llama3.2:1b - **1.3 GB**
```{bash}
ollama run llama3.2:1b
```
llama3.2:3b - **2.0GB**
```{bash}
ollama run llama3.2:3b
```

1. TinyLlama - **637 MB**
* Text-only model
```{bash}
$raspberry-pi-ollama % ollama run tinyllama
pulling manifest 
pulling 2af3b81862c6... 100% ▕██████████████████████████████████████████████████████████████████████████████████████████████████████████▏ 637 MB                         
pulling af0ddbdaaa26... 100% ▕██████████████████████████████████████████████████████████████████████████████████████████████████████████▏   70 B                         
pulling c8472cd9daed... 100% ▕██████████████████████████████████████████████████████████████████████████████████████████████████████████▏   31 B                         
pulling fa956ab37b8c... 100% ▕██████████████████████████████████████████████████████████████████████████████████████████████████████████▏   98 B                         
pulling 6331358be52a... 100% ▕██████████████████████████████████████████████████████████████████████████████████████████████████████████▏  483 B                         
verifying sha256 digest 
writing manifest 
success 
```
2. Phi - **1.6GB**
* Text-only model
```{bash}
$raspberry-pi-ollama % ollama run phi
pulling manifest 
pulling 04778965089b... 100% ▕██████████████████████████████████████████████████████████████████████████████████████████████████████████▏ 1.6 GB                         
pulling 7908abcab772... 100% ▕██████████████████████████████████████████████████████████████████████████████████████████████████████████▏ 1.0 KB                         
pulling 774a15e6f1e5... 100% ▕██████████████████████████████████████████████████████████████████████████████████████████████████████████▏   77 B                         
pulling 3188becd6bae... 100% ▕██████████████████████████████████████████████████████████████████████████████████████████████████████████▏  132 B                         
pulling 0b8127ddf5ee... 100% ▕██████████████████████████████████████████████████████████████████████████████████████████████████████████▏   42 B                         
pulling 4ce4b16d33a3... 100% ▕██████████████████████████████████████████████████████████████████████████████████████████████████████████▏  555 B                         
verifying sha256 digest 
writing manifest 
success 
```
3. Llava - **4.7GB**
* Vision enabled - analyze image in given path
```{bash}
$raspberry-pi-ollama % ollama run llava
pulling manifest 
pulling 170370233dd5... 100% ▕██████████████████████████████████████████████████████████████████████████████████████████████████████████▏ 4.1 GB                         
pulling 72d6f08a42f6... 100% ▕██████████████████████████████████████████████████████████████████████████████████████████████████████████▏ 624 MB                         
pulling 43070e2d4e53... 100% ▕██████████████████████████████████████████████████████████████████████████████████████████████████████████▏  11 KB                         
pulling c43332387573... 100% ▕██████████████████████████████████████████████████████████████████████████████████████████████████████████▏   67 B                         
pulling ed11eda7790d... 100% ▕██████████████████████████████████████████████████████████████████████████████████████████████████████████▏   30 B                         
pulling 7c658f9561e5... 100% ▕██████████████████████████████████████████████████████████████████████████████████████████████████████████▏  564 B                         
verifying sha256 digest 
writing manifest 
success
```

---

## Deployment
Use the `./llm.py` script - 
