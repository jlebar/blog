#!/bin/sh
#
# Create Weblog's distribution tarball
#

if [ -z ${1} ]
then
        echo "Usage: ${0} version"; exit 1
else
        version=${1}
fi

dir='/tmp/weblog'

mkdir -p ${dir}

# Normal version
hg archive -t tgz ${dir}/weblog-${version}.tar.gz

# Standalone version
standalone_basename="weblog+jinja2+markdown2-${version}"
standalone_dir="${dir}/${standalone_basename}"
license="${standalone_dir}/COPYING"

rm -rf ${standalone_dir}
hg archive -t files ${standalone_dir}

jinja_version=2.2.1
jinja_basename=Jinja2-${jinja_version}
jinja_filename=${jinja_basename}.tar.gz
jinja_url=http://pypi.python.org/packages/source/J/Jinja2/${jinja_filename}

if [ ! -r ${dir}/${jinja_filename} ]
then
        ftp -o ${dir}/${jinja_filename} ${jinja_url}
fi

tar zxf ${dir}/${jinja_filename} -C ${dir}
mkdir -p ${standalone_dir}/jinja2
cp -r ${dir}/${jinja_basename}/jinja2/*.py ${standalone_dir}/jinja2

echo >> ${license}
echo 'Jinja 2 license:' >> ${license}
# Jinja LICENSE is a dos file ...
awk '{ sub("\r$", ""); print }' ${dir}/${jinja_basename}/LICENSE >> ${license}
echo >> ${license}
echo 'Jinja 2 authors:' >> ${license}
cat ${dir}/${jinja_basename}/AUTHORS >> ${license}

markdown2_version=1.0.1.15
markdown2_basename=markdown2-${markdown2_version}
markdown2_filename=${markdown2_basename}.zip
markdown2_url=http://pypi.python.org/packages/source/m/markdown2/${markdown2_filename}

if [ ! -r ${dir}/${markdown2_filename} ]
then
        ftp -o ${dir}/${markdown2_filename} ${markdown2_url}
fi

unzip -qo ${dir}/${markdown2_filename} -d ${dir}
cp ${dir}/${markdown2_basename}/lib/markdown2.py ${standalone_dir}/

echo >> ${license}
echo 'Markdown 2 license:' >> ${license}
cat ${dir}/${markdown2_basename}/LICENSE.txt >> ${license}

tar zcf ${dir}/${standalone_basename}.tar.gz -C ${dir} ${standalone_basename}

echo "Don't forget to check: INSTALL, weblog/__init__.py"
hg tags | fgrep -q "${version}" || echo "CHECK TAGS"
echo 'To upload to PyPi: python setup.py sdist upload --sign'
