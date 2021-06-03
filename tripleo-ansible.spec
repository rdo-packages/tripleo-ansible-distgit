# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %{expand:%{python%{pyver}_sitelib}}
%global pyver_install %{expand:%{py%{pyver}_install}}
%global pyver_build %{expand:%{py%{pyver}_build}}
# End of macros for py2/py3 compatibility

%global srcname tripleo_ansible
%global rolename tripleo-ansible

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           %{rolename}
Version:        0.7.0
Release:        1%{?dist}
Summary:        Ansible project for TripleO

Group:          System Environment/Base
License:        ASL 2.0
URL:            https://git.openstack.org/cgit/openstack/tripleo-ansible
Source0:        https://github.com/openstack/%{rolename}/archive/%{upstream_version}.tar.gz

BuildArch:      noarch
BuildRequires:  git
BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-setuptools
BuildRequires:  python%{pyver}-pbr
BuildRequires:  python%{pyver}-jinja2 >= 2.8.0
%if %{pyver} == 2
BuildRequires: PyYAML
%else
BuildRequires: python%{pyver}-PyYAML
%endif

Requires: ansible >= 2.8.0
Requires: ansible-collections-openstack >= 1.3.0
Requires: ansible-config_template
Requires: ansible-role-openstack-operations
Requires: python%{pyver}-paunch
Requires: python%{pyver}-jinja2 >= 2.8.0

%description

Ansible project for TripleO

%prep
%autosetup -n %{rolename}-%{upstream_version} -S git


%build
%{pyver_build}


%install
export PBR_VERSION=%{version}
export SKIP_PIP_INSTALL=1
%{pyver_install}


%files
%doc README*
%license LICENSE
%{pyver_sitelib}/%{srcname}-*.egg-info
%{_datadir}/ansible/


%changelog
* Mon Apr 05 2021 RDO <dev@lists.rdoproject.org> 0.7.0-1
- Update to 0.7.0

* Mon Feb 08 2021 RDO <dev@lists.rdoproject.org> 0.6.0-1
- Update to 0.6.0

* Thu Apr 09 2020 RDO <dev@lists.rdoproject.org> 0.5.0-1
- Update to 0.5.0

* Mon Jan 06 2020 RDO <dev@lists.rdoproject.org> 0.4.1-1
- Update to 0.4.1

* Mon Oct 21 2019 RDO <dev@lists.rdoproject.org> 0.4.0-1
- Update to 0.4.0


