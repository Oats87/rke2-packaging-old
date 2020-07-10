%global ARCH amd64

Name:    rke2-common
Version: %{rpm_version}
Release: %{rpm_release}%{?dist}
Summary: RKE2 Common Files

Group:   System Environment/Base		
License: ASL 2.0
URL:     https://rancher.com
Source0: https://github.com/rancher/rke2/releases/download/%{rke2_version}/rke2-%{rke2_version}.linux-%{ARCH}

BuildRequires: systemd
Requires(post): rke2-selinux >= %{rke2_policyver}

%description
The Next Generation Rancher Labs Distribution of Kubernetes

%prep
cp -p %SOURCE0 %{_builddir}/rke2

%install
cd %{_builddir}
install -m 755 -d %{buildroot}%{_bindir}
install -p -m 755 -t %{buildroot}%{_bindir}/ rke2
install -d %{buildroot}%{_sysconfdir}/rke2

%files
%{_bindir}/rke2
%{_sysconfdir}/rke2/

%changelog
* Thu Jul 9 2020 Chris Kim <oats87g@gmail.com.com> 0.1-1
- Initial version
