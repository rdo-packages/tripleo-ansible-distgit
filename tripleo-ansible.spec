# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
# End of macros for py2/py3 compatibility

%global srcname tripleo_ansible
%global rolename tripleo-ansible

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           %{rolename}
Version:        0.1.0
Release:        1%{?dist}
Summary:        Ansible project for TripleO

Group:          System Environment/Base
License:        ASL 2.0
URL:            https://opendev.org/openstack/tripleo-ansible
Source0:        https://github.com/openstack/%{rolename}/archive/%{upstream_version}.tar.gz

BuildArch:      noarch
BuildRequires:  git
BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-setuptools
BuildRequires:  python%{pyver}-pbr

# Handle python2 exception
%if %{pyver} == 2
BuildRequires:  python-d2to1
Requires:       ansible
%else
BuildRequires:  python%{pyver}-d2to1
Requires:       ansible-python%{pyver}
%endif


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
* Mon Apr 22 2019 RDO <dev@lists.rdoproject.org> 0.1.0-1
- Update to 0.1.0


# REMOVEME: error caused by commit https://opendev.org/openstack/tripleo-ansible/commit/7d5a361fbceafe4b0741f81b5fba5d3000a59867
