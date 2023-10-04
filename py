[python-custom]
name=Custom Python Repository
{% if os_version == '7' %}
baseurl=http://example.com/python-repo/rhel7/x86_64/
{% elif os_version == '8' %}
baseurl=http://example.com/python-repo/rhel8/x86_64/
{% else %}
# Handle unsupported OS versions here
baseurl=
{% endif %}
enabled=1
gpgcheck=0
