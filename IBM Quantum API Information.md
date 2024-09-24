
## Make sure your IBM Quantum API is activated

In order to run code on IBM Quantum, we need to connect our code to the IBM Quantum service. This can be accomplished by activating your IBM Quantum API token. In lay terms, an API, or Application Programming Interface, is a bridge that connects two programs. It allows one program to request functions/data from another. In our present case, we want to connect our code written with qiskit to the IBM Quantum systems so that we can implement Bells Inequality on an actual quantum computer.

This can be done by including the line 

```python
QiskitRuntimeService.save_account(token="YOUR_API_TOKEN", channel="ibm_quantum")
```

after the 

```python
from qiskit_ibm_runtime import QiskitRuntimeService
```

statement. If the code you're working on is exclusively private and not published anywhere, you can directly copy and paste your token into this line of code. If, however, the code you're using is public, _do not do this_. Instead, you can use something like Codespace Secrets to initialize your service. You can do that using the following steps (which I took directly from https://github.com/ubsuny/CompPhys/tree/main/qiskit):

1. In the upper-right corner of any page on GitHub, click your profile photo, then click Settings.

2. In the "Code, planning, and automation" section of the sidebar, click  Codespaces.

3. To the right of "Codespaces secrets", click New secret.

4. Under "Name," type a name for your secret, use *IBMQUANTUM*.

5. Under "Value", copy the API key from your IBM quantum profile.

6. Select the "Repository access" drop-down menu, then click a repository you want to have access to the secret. Repeat for every repository you want to have access to the secret.

You can find your API token in the top right of the screen after by going to ibm.com/quantum and signing in. There's a button that allows you to copy the token to your clipboard. 

This line only needs to be run once. It will update your local configuration file which holds all of your qiskit and IBM Quantum credentials. On windows the configuration file is usually located at: C:\Users\YourUsername\.qiskit\qiskitrc. On Mac it's /home/YourUsername/.qiskit/qiskitrc.

Once the configuration file has been updated (i.e. you've run that line of code), you can simply use the line **service = QiskitRuntimeService()** to set up the connection between your code (qiskit in this case) and IBM Quantum's cloud services. This will work in any python file or github codespace you use.
