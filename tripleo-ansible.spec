
%global srcname tripleo_ansible
%global rolename tripleo-ansible

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           %{rolename}
Version:        1.5.1
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

Requires: ansible >= 2.9.10
Requires: ansible-config_template
Requires: ansible-role-openstack-operations
Requires: python3-paunch
Requires: python3-jinja2 >= 2.8.0
Requires: python3-tripleo-common
Requires: python3-ironicclient
Requires: python3-glanceclient

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
* Mon Oct 05 2020 RDO <dev@lists.rdoproject.org> 1.5.1-1
- Update to 1.5.1

* Tue Jul 28 2020 RDO <dev@lists.rdoproject.org> 1.5.0-1
- Update to 1.5.0

* Tue May 26 2020 RDO <dev@lists.rdoproject.org> 1.4.0-1
- Update to 1.4.0

