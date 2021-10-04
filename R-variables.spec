#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-variables
Version  : 1.1.1
Release  : 1
URL      : https://cran.r-project.org/src/contrib/variables_1.1-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/variables_1.1-1.tar.gz
Summary  : Variable Descriptions
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n variables
cd %{_builddir}/variables

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1633385666

%install
export SOURCE_DATE_EPOCH=1633385666
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library variables
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library variables
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library variables
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc variables || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/variables/CITATION
/usr/lib64/R/library/variables/DESCRIPTION
/usr/lib64/R/library/variables/INDEX
/usr/lib64/R/library/variables/Meta/Rd.rds
/usr/lib64/R/library/variables/Meta/features.rds
/usr/lib64/R/library/variables/Meta/hsearch.rds
/usr/lib64/R/library/variables/Meta/links.rds
/usr/lib64/R/library/variables/Meta/nsInfo.rds
/usr/lib64/R/library/variables/Meta/package.rds
/usr/lib64/R/library/variables/NAMESPACE
/usr/lib64/R/library/variables/NEWS.Rd
/usr/lib64/R/library/variables/R/variables
/usr/lib64/R/library/variables/R/variables.rdb
/usr/lib64/R/library/variables/R/variables.rdx
/usr/lib64/R/library/variables/help/AnIndex
/usr/lib64/R/library/variables/help/aliases.rds
/usr/lib64/R/library/variables/help/paths.rds
/usr/lib64/R/library/variables/help/variables.rdb
/usr/lib64/R/library/variables/help/variables.rdx
/usr/lib64/R/library/variables/html/00Index.html
/usr/lib64/R/library/variables/html/R.css
/usr/lib64/R/library/variables/tests/regtests.R
/usr/lib64/R/library/variables/tests/regtests.Rout.save