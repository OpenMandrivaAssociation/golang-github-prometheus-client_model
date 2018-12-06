%bcond_without check
%global goipath     github.com/prometheus/client_model
%global commit      99fa1f4be8e564e8a6b613da7fa6f46c9edafc6c

Version:            0

%global common_description %{expand:
Data model artifacts for Prometheus.}

%gometa

Name:    golang-github-prometheus-client_model
Release: 0.16%{?dist}
Summary: Data model artifacts for Prometheus
License: ASL 2.0
URL:     %{gourl}
Source:  %{gosource}

BuildRequires: golang(github.com/golang/protobuf/proto)


%description
%{common_description}

%package   devel
Summary:   %{summary}
BuildArch: noarch

%description devel
%{common_description}

This package contains the source code needed for building packages that import
the %{goipath} Go namespace.

%prep
%gosetup -q
rm -rf vendor

%install
%goinstall glide.lock glide.yaml

%check
%if %{with check}
  %gochecks
%endif

%files devel -f devel.file-list
%license LICENSE NOTICE
%doc CONTRIBUTING.md MAINTAINERS.md README.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16.git99fa1f4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 26 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.15.git99fa1f4
- Upload glide files

* Fri May 25 2018 Paul Gier <pgier@redhat.com> - 0-0.14.20180525git99fa1f4
- Update to latest snapshot version 99fa1f4be8e564e8a6b613da7fa6f46c9edafc6c
- Update spec to current Go packaging standards

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.git6f38060
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 22 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.12.git6f38060
- Bump to upstream 6f3806018612930941127f2a7c6c453ba2c527d2
  related: #1250496

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.gitfa8ad6f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.gitfa8ad6f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.gitfa8ad6f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.gitfa8ad6f
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.gitfa8ad6f
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.gitfa8ad6f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Aug 07 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.5.gitfa8ad6f
- Update spec file to spec-2.0
  resolves: #1250496

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.gitfa8ad6f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 05 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.gitfa8ad6f
- Update build-time dependencies
  related: #1190437

* Wed Mar 04 2015 jchaloup <jchaloup@redhat.com> - 0-0.2.gitfa8ad6f
- Bump to upstream fa8ad6fec33561be4280a8f0514318c79d7f6cb6
  related: #1190437

* Sat Feb 07 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.gitbc9454c
- First package for Fedora
  resolves: #1190437
