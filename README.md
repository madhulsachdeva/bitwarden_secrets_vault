## Secrets Done Right with Bitwarden Secrets Manager.

### How to separate secrets from source code using Bitwarden Secrets Manager Instead of .env Files

As developers, we often store our secrets (API keys, access tokens etc.) in the .env file for convenience. While adding .env to .gitignore is good practice so your secrets are not checked in, you are still storing your secrets with your source. This is akin to storing your MFA recovery codes along with your password.

According to security best practices, secrets must be managed and stored separately from your source code so they are not compromised in the event of a breach and can be rotated without affecting your code.

This repository contains the steps for importing your BWS Secrets into your source code along with the boilerplate code needed for Python modules. 

This should be easily transferable to other languages as we are using the CLI option.

You can learn more about **Bitwarden Secrets Manager** here: https://bitwarden.com/help/secrets-manager-overview/

## STEPS TO IMPORT BWS SECRETS BELOW:

### 1. Install BWS CLI:

```curl https://bws.bitwarden.com/install | sh```

### 2. Export BWS Access token  
(or store it in .env if you really want to do that)

#### For .env
```BWS_ACCESS_TOKEN=<your-access-token>```

#### OR export it as environment variable

```export BWS_ACCESS_TOKEN=<your-access-token>```

### 3. Copy the attached boilerplate code to your project in module called bws_secrets.py
--> For code reference **bws_secrets.py** file

### 4. Import your secrets from BWS vault instead of .env file as shown below (see below for example)
```
from utils.bws_secrets import get_secret
OPEN_API_KEY = get_secret("49c5c198-5078-44b7-abc8-42231a-cd30acc")
```

#### Note:

**49c5c198-5078-44b7-abc8-42231a-cd30acc** is the secret ID from the BWS Secret you want to import from your BWS Secrets Manager vault. 

_This is not a real BWS secret ID, only used for illustration purposes._

### Conclusion

Rotating secrets is as simple as updating the the value associated with your secret key in the BWS Secrets Manager vault.

Using this approach allows you to rotate the secrets through the BWS vault service and ensure that your code always has access to the latest secrets.

#### Disclaimer: 
I am not associated with Bitwarden and this my independent view and experience. Please do your own due diligence before implementing in production as I cannot be held liable for any damage caused as a result of using this code.
