# Ganache Setup Guide

This guide describes how to run Ganache to support the blockchain component of the voting system.

## 1. Installation
1.  Download the **Ganache GUI** from the [Truffle Suite website](https://trufflesuite.com/ganache/).
2.  Install and launch the application on your computer.

## 2. Launching Ganache
1.  Open the Ganache application.
2.  Select **"QUICKSTART"** for a fast setup, or create a **"New Workspace"** to persist your settings.

## 3. Mandatory Configuration
To ensure the voting system can connect, verify the following settings:
- **RPC Server**: `HTTP://127.0.0.1:7545`
- **Port**: `7545`
- **Network ID / Chain ID**: `1337` (Default for Ganache)

> [!TIP]
> This project is configured to use port `7545`. If you use the default `8545` port, the connection will fail unless you update `settings.py`.

## 4. Verifying the Connection
Once Ganache is running (you should see a list of 10 addresses with 100 ETH each):
1.  Open your terminal/command prompt.
2.  Activate your virtual environment: `voting_venv\Scripts\activate`.
3.  Run the test script:
    ```bash
    python test_ganache_connection.py
    ```
4.  If it returns **"Connected to Ganache!"**, you are ready to proceed with the project steps (migrations, runserver, etc.).

## 5. Next Steps
Once Ganache is connected:
- Run migrations: `python manage.py migrate`
- Start the server: `python manage.py runserver`
- Access the Admin Panel to deploy the voting contract as needed.
