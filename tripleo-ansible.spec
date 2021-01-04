
%global srcname tripleo_ansible
%global rolename tripleo-ansible

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           %{rolename}
Version:        2.1.0
Release:        1%{?dist}
Summary:        Ansible project for TripleO

Group:          System Environment/Base
License:        ASL 2.0
URL:            https://git.openstack.org/cgit/openstack/tripleo-ansible
Source0:        https://github.com/openstack/%{rolename}/archive/%{upstream_version}.tar.gz

BuildArch:      noarch
BuildRequires:  git
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr
BuildRequires:  python3-jinja2 >= 2.8.0
BuildRequires:  python3-PyYAML
BuildRequires:  python3-metalsmith

Requires: ansible >= 2.9.10
Requires: ansible-config_template
Requires: ansible-role-metalsmith-deployment >= 1.2.0
Requires: ansible-role-openstack-operations
Requires: python3-jinja2 >= 2.8.0
Requires: python3-tripleo-common
Requires: python3-ironicclient
Requires: python3-glanceclient
Requires: python3-metalsmith >= 1.2.0

%description

Ansible project for TripleO

%prep
%autosetup -n %{rolename}-%{upstream_version} -S git


%build
%{py3_build}


%install
export PBR_VERSION=%{version}
export SKIP_PIP_INSTALL=1
%{py3_install}


%files
%doc README*
%license LICENSE
%{python3_sitelib}/%{srcname}-*.egg-info
%{_datadir}/ansible/


%changelog
* Mon Jan 04 2021 RDO <dev@lists.rdoproject.org> 2.1.0-1
- Update to 2.1.0

* Mon Nov 02 2020 RDO <dev@lists.rdoproject.org> 2.0.0-1
- Update to 2.0.0

