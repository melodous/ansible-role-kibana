Welcome to kibana Ansible Role’s documentation!
===============================================

Kibana
------

Ansible role to install and configure Kibana as container

### Requirements

Docker

### Dependencies

N/A

### Example Playbook

    - hosts: servers
      roles:
        - { role: kibana }

pip ansible role default variables
----------------------------------

#### Sections

-   kibana packaging
-   Kibana configuration
-   Kibana monitoring management

### kibana packaging

`kibana_docker_imagen`

> Kibana docker image

    kibana_docker_image: melodous/kibana

`kibana_version`

> Kibana docker image version (TAG)

    kibana_version: 5.4.1

`kibana_docker_labels`

> Yaml dictionary which maps Docker labels. os\_environment: Name of the
> environment, example: Production, by default “default”.
> os\_contianer\_type: Type of the container, by default kibana.

    kibana_docker_labels:
      os_environment: "{{ docker_os_environment | default('default') }}"
      os_contianer_type: kibana

### Kibana configuration

`kibana_group`

> Kibana group name

    kibana_group: kibana

`kibana_group_id`

> Kibana group id

    kibana_group_id: 1000

`kibana_user`

> Kibana user name

    kibana_user: kibana

`kibana_user_id`

> Kibana user id

    kibana_user_id: 1000

`conf_dir`

> Configuration directory

    conf_dir: /etc/kibana

### Kibana monitoring management

`kibana_monitoring`

> Enable or disable kibana monitoring
>
>     kibana_monitoring: true

Changelog
---------

**kibana**

This project adheres to Semantic Versioning and human-readable
changelog.

### kibana master - unreleased

##### Added

-   First addition

##### Changed

-   First change

### kibana v0.0.1 - 2017/07/13

##### Added

-   Initial version

Copyright
---------

kibana

Copyright (C) 2017/07/13 Raúl Melo
&lt;<raul.melo@opensolutions.cloud>&gt;

LICENSE
