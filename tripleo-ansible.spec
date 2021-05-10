
%global srcname tripleo_ansible
%global rolename tripleo-ansible

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           %{rolename}
Version:        1.5.3
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
Requires: ansible-collections-openstack >= 1.3.0
Requires: ansible-collection-ansible-netcommon >= 1.5.0
Requires: ansible-collection-ansible-posix >= 1.2.0
Requires: ansible-collection-community-general >= 2.5.1
Requires: ansible-collection-containers-podman >= 1.4.1
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
* Wed Apr 14 2021 RDO <dev@lists.rdoproject.org> 1.5.3-1
- Update to 1.5.3

* Thu Jan 28 2021 RDO <dev@lists.rdoproject.org> 1.5.2-1
- Update to 1.5.2

* Mon Oct 05 2020 RDO <dev@lists.rdoproject.org> 1.5.1-1
- Update to 1.5.1

* Tue Jul 28 2020 RDO <dev@lists.rdoproject.org> 1.5.0-1
- Update to 1.5.0

* Tue May 26 2020 RDO <dev@lists.rdoproject.org> 1.4.0-1
- Update to 1.4.0

