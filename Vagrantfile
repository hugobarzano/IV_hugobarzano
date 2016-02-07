Vagrant.configure('2') do |config|

  config.vm.define "localhost" do |l|
    l.vm.hostname = "localhost"
    l.vm.box = 'azure'
    l.vm.network "public_network"
    l.vm.network "private_network",ip: "192.168.56.10", virtualbox__intnet: "vboxnet0"
    l.vm.network "forwarded_port", guest: 80, host: 80

    l.vm.provider :azure do |azure, override|
 	azure.mgmt_certificate = File.expand_path('~/.ssh/azurevagrant.pem')
 	azure.mgmt_endpoint = 'https://management.core.windows.net'
 	azure.subscription_id = 'b0eda1f9-f644-4cfd-bc55-29015eed62c9'
 	azure.vm_image = 'b39f27a8b8c64d52b05eac6a62ebad85__Ubuntu-14_04_2-LTS-amd64-server-20150506-en-us-30GB'
 	azure.vm_name = 'computermanagementansibleapp'
  azure.cloud_service_name = 'computermanagementansibleapp'
 	azure.vm_password = 'Clave#Hugo#1'
 	azure.vm_location = 'Central US'
 	azure.ssh_port = '22'
 	azure.tcp_endpoints = '80:80'
 	end
     l.vm.provision "ansible" do |ansible|
    	ansible.sudo = true
    	ansible.playbook = "playbook.yml"
    	ansible.verbose = "vvv"
    	ansible.host_key_checking = false
  	end
 end

  config.vm.define "localhost2" do |l2|
    l2.vm.hostname = "localhost2"
    l2.vm.box = 'azure'
    l2.vm.network "public_network"
    l2.vm.network "private_network",ip: "192.168.56.11", virtualbox__intnet: "vboxnet0"
    l2.vm.network "forwarded_port", guest: 80, host: 80

    l2.vm.provider :azure do |azure, override|
 	azure.mgmt_certificate = File.expand_path('~/.ssh/azurevagrant.pem')
 	azure.mgmt_endpoint = 'https://management.core.windows.net'
 	azure.subscription_id = 'b0eda1f9-f644-4cfd-bc55-29015eed62c9'
 	azure.vm_image = 'b39f27a8b8c64d52b05eac6a62ebad85__Ubuntu-14_04_2-LTS-amd64-server-20150506-en-us-30GB'
 	azure.vm_name = 'computerManagementDockerApp'
  azure.cloud_service_name = 'computerManagementDockerApp'
 	azure.vm_password = 'Clave#Hugo#2'
 	azure.vm_location = 'Central US'
 	azure.ssh_port = '22'
  azure.tcp_endpoints = '80:80'
 	end
     l2.vm.provision "ansible" do |ansible|
    	ansible.sudo = true
    	ansible.playbook = "playbook2.yml"
    	ansible.verbose = "vvv"
    	ansible.host_key_checking = false
  	end
 end


end
