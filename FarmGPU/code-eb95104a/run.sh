export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libtcmalloc_minimal.so.4
export DATADIR=/mnt/wk0/train/unet3d
export MLPERF_ORGNAME=farmgpu
for i in {1..4}; do
	./mlpstorage closed training unet3d run file --hosts 10.100.200.46 10.100.200.47 10.100.200.48 10.100.200.49 10.100.200.50 10.100.200.51 10.100.200.52 10.100.200.53 10.100.200.26 10.100.200.27 10.100.200.28 10.100.200.29 10.100.200.30 10.100.200.31 10.100.200.32 --exec-type=mpi --mpi-params="-x LD_PRELOAD=$LD_PRELOAD" -na=75 -cm=1007 -at=b200 --results-dir=/mnt/mlperf_results/ --data-dir=$DATADIR --systemname=hickory --params reader.read_threads=16 reader.odirect=True reader.prefetch_size=0 dataset.num_files_train=553166 dataset.total_disk_bytes=81094482988248 dataset.skip_listing=True dataset.listing_validation_interval=100 dataset.num_subfolders_train=55 --allow-run-as-root;
	for host in 10.100.200.46 10.100.200.47 10.100.200.48 10.100.200.49 10.100.200.50 10.100.200.51 10.100.200.52 10.100.200.53 10.100.200.26 10.100.200.27 10.100.200.28 10.100.200.29 10.100.200.30 10.100.200.31 10.100.200.32; do
		ssh -i /home/fgpu/.ssh/weka_id_rsa fgpu@$host sudo pkill -9 mpi;
	done;
	sleep 5;
done
