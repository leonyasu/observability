##########################################################################################
# SA Bootcamp 2024 - Observability
##########################################################################################

##  Demos and Labs

Objectives:
    - Understand metrics, logs and traces
    - Configure and setup Prometheus
    - Create dashboards in Grafana
    - Work with ADOT add-on on EKS
    
Requirements:
    - Cloud9
    - Python3
    - CloudWatch
    - Prometheus
    - Grafana

##########################################################################################
## Lab Setup    
##########################################################################################

1/ Create a Cloud9 environment

AWS Cloud9 > Environments > Create environment

- name: SA-bootcamp
- New EC2 Instance : t3.small (2 GiB RAM + 2 vCPU)
- Platform: Amazon Linux 2023
- Timeout: 4h

git clone https://github.com/leonyasu/observability.git

##########################################################################################
## Lab 1: Collecting metrics and logs with python and boto3 + trace with xRay
##########################################################################################

1/ Create a python3 file
    
    vi Lab_1A.py 

2/ Install boto3

    pip3 install boto3

3/ Run the code 

    python3 Lab_1A.py 
    python3 Lab_1A.py | grep Dimension

4/ Verify metrics
    
    Go to AWS console
    
5/ Run the code
    
    python3 Lab_1B.py 
    python3 Lab_1B.py | grep Dimension

6/ Verify logs

    Go to AWS Console
    
7/ Install x-ray daemon

    https://docs.aws.amazon.com/pt_br/xray/latest/devguide/xray-daemon.html

    pip install aws-xray-sdk

    export AWS_XRAY_DAEMON_ADDRESS=127.0.0.1:2000

8/ Run the code

    python3 Lab_1C.py 
    python3 Lab_1C.py | grep Dimension

9/ Verify console

    X-Ray traces > traces

https://docs.aws.amazon.com/pt_br/xray/latest/devguide/xray-sdk-python.html

https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-python-middleware.html

https://docs.aws.amazon.com/pt_br/xray/latest/devguide/xray-sdk-python-configuration.html

https://github.com/aws/aws-xray-sdk-python

##########################################################################################
## Lab 2: Integration with Amazon Managed Prometheus
##########################################################################################

Lab_2.txt

https://prometheus.io/

https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-onboard-ingest-metrics-remote-write-EC2.html

wget https://github.com/prometheus/prometheus/releases/download/v2.51.1/prometheus-2.51.1.linux-amd64.tar.gz

wget https://github.com/prometheus/node_exporter/releases/download/v1.7.0/node_exporter-1.7.0.linux-amd64.tar.gz


##########################################################################################
## Lab 3: Generating Dashboard with Amazon Managed Grafana
##########################################################################################

Lab_3.txt

https://grafana.com/

https://grafana.com/grafana/download?pg=get&plcmt=selfmanaged-box1-cta1

wget https://dl.grafana.com/enterprise/release/grafana-enterprise-10.4.1.linux-amd64.tar.gz

tar -zxvf grafana-enterprise-10.4.1.linux-amd64.tar.gz

##########################################################################################
##Lab 4: ADOT add-on on EKS
##########################################################################################

Lab_4.txt

ADOT
ADOT + EKS
   
   
   
   
   
   