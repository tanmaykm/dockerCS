LOCAL_DATA_DIR=`pwd`
echo "Mounting local directory $LOCAL_DATA_DIR as /data/csRun"
echo "Circuitscape configuration: $1"
echo "docker run --name csrun -v ${LOCAL_DATA_DIR}:/data -i tanmaykm/circuitscape:v1 csrun.py $1"
docker rm csrun
docker run --name csrun -v ${LOCAL_DATA_DIR}:/data -i tanmaykm/circuitscape:v1 csrun.py $1
#docker run --name csrun -v ${LOCAL_DATA_DIR}:/data/csRun csrun.py $1
