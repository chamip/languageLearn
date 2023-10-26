import numpy as np
import sys
import os
import datetime
from astropy.io import fits
import argparse
from functools import partial

calD = 4.148808e3
freq_low = 1000.
bandwidth = 500.
nchan = 4096
freqs = np.linspace(freq_low, freq_low + bandwidth, nchan, endpoint=False)
freq_center = freq_low + (bandwidth - bandwidth/float(nchan))/2.
freq_ref = freq_low + bandwidth - bandwidth/float(nchan)

nsubint_advance = 2
nsubint_delay = 2

def mjd_find(fitsname_list, burst_mjd_list, dm_list):
    # 这里可以打印传入的参数看看是否符合预期
    print("... mjd_find function ...")
    print("fitsname_list: ", fitsname_list)
    print("burst_mjd_list: ", burst_mjd_list)
    print("dm_list: ", dm_list)
    print("... mjd_find function ...")
    print("fitsname_list[0]: ", fitsname_list[0])
    flag = False
    burst_filename_index, burst_filename, burst_subint, burst_bin, = -1, 'None', -1, -1
    for i,fitsname in enumerate(fitsname_list):
        print('searching mjd in %s'%fitsname)
    # 报错在下面这行，fits就是前面的astropy.io，通过它打开文件b.ar
    with fits.open(fitsname_list[0]) as hdul:
        print("fitsname_list[0]: ", fitsname_list[0])
        nsubint = hdul['SUBINT'].header['NAXIS2']
        stt_imjd = hdul[0].header['STT_IMJD']
        stt_smjd = hdul[0].header['STT_SMJD']
        stt_offs = hdul[0].header['STT_OFFS']
        tsubint = hdul['SUBINT'].data['TSUBINT'][0]
        offs_sub = hdul['SUBINT'].data['OFFS_SUB']
        stt_obs = stt_imjd + (stt_smjd + stt_offs + offs_sub[0] - tsubint/2.)/86400.
        nbin = hdul['SUBINT'].header['NSBLK']
        tbin = tsubint/float(nbin)
        time_length_file = tsubint*nsubint

    arg_list = []
    for i, burst_mjd in enumerate(burst_mjd_list):
        burst_filename_index = int(np.floor((burst_mjd - stt_obs)*86400./time_length_file))
        burst_subint = int(np.floor(((burst_mjd - stt_obs)*86400. - burst_filename_index*time_length_file)/tsubint))
        burst_bin = int(np.round(((burst_mjd - stt_obs)*86400. - burst_filename_index*time_length_file - burst_subint*tsubint)/tbin))
        arg_list.append([burst_mjd, burst_filename_index, burst_subint, burst_bin, dm_list[i]])
    return(arg_list)


def history(fits_hdul, nbin, tbin, dm):
    print('generate history hdu', nbin, tbin)
    hdr = fits.Header()
    hdr['EXTNAME'] = ('HISTORY', 'name of this binary table extension')
    hdr['EXTVER'] = (1, 'auto assigned by template parser')
    date_pro = datetime.datetime.now().strftime('%c')
    col_date_pro = fits.Column(name='DATE_PRO', format='24A', array=[date_pro])
    col_proc_cmd = fits.Column(name='PROC_CMD', format='256A', array=['PYTHON'])
    col_scale = fits.Column(name='SCALE', format='8A', array=[fits_hdul['SUBINT'].header['SCALE']])
    col_pol_type = fits.Column(name='POL_TYPE', format='8A', array=[fits_hdul['SUBINT'].header['POL_TYPE']])
    col_nsub = fits.Column(name='NSUB', format='1J', array=[np.int32(1)])
    col_npol = fits.Column(name='NPOL', format='1I', array=[np.int16(fits_hdul['SUBINT'].header['NPOL'])])
    col_nbin = fits.Column(name='NBIN', format='1J', array=[np.int32(nbin)])
    col_nbin_prd = fits.Column(name='NBIN_PRD', format='1J', array=[np.int32(nbin)])
    col_tbin = fits.Column(name='TBIN', format='1D', array=[np.float64(tbin)])
    col_ctr_freq = fits.Column(name='CTR_FREQ', format='1D', array=[np.float64(freq_center)])
    col_nchan = fits.Column(name='NCHAN', format='1J', array=[np.int32(fits_hdul['SUBINT'].header['NCHAN'])])
    col_chan_bw = fits.Column(name='CHAN_BW', format='1D', array=[np.float64(fits_hdul['SUBINT'].header['CHAN_BW'])])
    col_ref_freq = fits.Column(name='REF_FREQ', format='1D', array=[np.float64(freq_ref)])
    col_dm = fits.Column(name='DM', format='1D', array=[np.float64(dm)])
    col_rm = fits.Column(name='RM', format='1D', array=[np.float64(0)])
    col_pr_corr = fits.Column(name='PR_CORR', format='1I', array=[np.int16(0)])
    col_fd_corr = fits.Column(name='FD_CORR', format='1I', array=[np.int16(0)])
    col_be_corr = fits.Column(name='BE_CORR', format='1I', array=[np.int16(0)])
    col_rm_corr = fits.Column(name='RM_CORR', format='1I', array=[np.int16(0)])
    col_dedisp = fits.Column(name='DEDISP', format='1I', array=[np.int16(1)])
    col_dds_mthd = fits.Column(name='DDS_MTHD', format='32A', array=['UNSET'])
    col_sc_mthd = fits.Column(name='SC_MTHD', format='32A', array=['NONE'])
    col_cal_mthd = fits.Column(name='CAL_MTHD', format='32A', array=['NONE'])
    col_cal_file = fits.Column(name='CAL_FILE', format='256A', array=['NONE'])
    col_rfi_mthd = fits.Column(name='RFI_MTHD', format='32A', array=['NONE'])
    col_rm_model = fits.Column(name='RM_MODEL', format='32A', array=['NONE'])
    col_aux_rm_c = fits.Column(name='AUX_RM_C', format='1I', array=[np.int16(0)])
    col_dm_model = fits.Column(name='DM_MODEL', format='32A', array=['NONE'])
    col_aux_dm_c = fits.Column(name='AUX_DM_C', format='1I', array=[np.int16(1)])
    cols = [col_date_pro, col_proc_cmd, col_scale, col_pol_type, col_nsub, col_npol, col_nbin, col_nbin_prd, col_tbin, col_ctr_freq, col_nchan, col_chan_bw, col_ref_freq, col_dm, col_rm, col_pr_corr, col_fd_corr, col_be_corr, col_rm_corr, col_dedisp, col_dds_mthd, col_sc_mthd,col_cal_mthd, col_cal_file, col_rfi_mthd, col_rm_model, col_aux_rm_c, col_dm_model, col_aux_dm_c]
    hdu = fits.BinTableHDU.from_columns(cols, header=hdr)
    print(hdu.data)
    return(hdu)


def data_norm(data_ori):
    npol, nchan, nbin = data_ori.shape
    data_norm = np.empty(data_ori.shape)
    dat_offs = np.empty(npol*nchan)
    dat_scl = np.empty(npol*nchan)
    data_max = data_ori.max(2)
    data_min = data_ori.min(2)
    dat_offs = np.float32((data_max + data_min)/2.)
    dat_scl = np.float32((data_max - data_min)/float(16384))
    data_norm = np.int16(np.round((data_ori - dat_offs[:, :, None])/dat_scl[:, :, None]))
    dat_offs = dat_offs.ravel()
    dat_scl = dat_scl.ravel()
    return(data_norm, dat_scl, dat_offs)

def subint(fits_hdul, st_filename_index, st_subint, st_bin, end_filename_index, end_subint, end_bin, dm, data_ori):
    print('generate subint hdu')
    fits_stt_imjd = fits_hdul[0].header['STT_IMJD']
    fits_stt_smjd = fits_hdul[0].header['STT_SMJD']
    fits_stt_offs = fits_hdul[0].header['STT_OFFS']
    fits_tsubint = fits_hdul['SUBINT'].data[st_subint]['TSUBINT']
    fits_offs_sub = fits_hdul['SUBINT'].data[st_subint]['OFFS_SUB']
    fits_nsubint = fits_hdul['SUBINT'].header['NAXIS2']
    fits_nbin = fits_hdul['SUBINT'].header['NSBLK']
    tbin = fits_tsubint/fits_nbin
    stt = fits_stt_imjd + (fits_stt_smjd + fits_stt_offs + fits_offs_sub - fits_tsubint/2 + st_bin*tbin)/86400.
    #tsubint = ((end_filename_index - st_filename_index)*fits_nsubint + (end_subint - st_subint))*fits_tsubint + (end_bin - st_bin)*tbin
    tsubint = tbin*data_ori.shape[2]
    offs_sub = tsubint/2.
    dat_freq = fits_hdul['SUBINT'].data[0]['DAT_FREQ']
    dat_wts = fits_hdul['SUBINT'].data[0]['DAT_WTS']
    data, dat_scl, dat_offs = data_norm(data_ori)
    nchan = len(dat_freq)
    hdr = fits.Header()
    hdr['EXTNAME'] = ('SUBINT', 'name of this binary table extension ')
    hdr['EPOCHS'] = ('VALID', 'Epoch convention (VALID, MIDTIME, STT_MJD)')
    hdr['INT_TYPE'] = ('TIME', 'Time axis (TIME, BINPHSPERI, BINLNGASC, etc)')
    hdr['INT_UNIT'] = ('SEC', 'Unit of time axis (SEC, PHS (0-1), DEG)')
    hdr['SCALE'] = ('FluxDen', 'Intensity units (FluxDen/RefFlux/Jansky)')
    hdr['POL_TYPE'] = (fits_hdul['SUBINT'].header['POL_TYPE'], 'Polarisation identifier (e.g., AABBCRCI, AA+BB)')
    print(data.shape)
    hdr['NPOL'] = (data.shape[-3], 'Nr of polarisations')
    hdr['TBIN'] = (tbin, '[s] Time per bin or sample')
    hdr['NBIN'] = (data.shape[-1], 'Nr of bins (PSR/CAL mode; else 1)')
    hdr['NBIN_PRD'] = ('*', 'Nr of bins/pulse period (for gated data)')
    hdr['PHS_OFFS'] = ('*', 'Phase offset of bin 0 for gated data')
    hdr['NBITS'] = (fits_hdul['SUBINT'].header['NBITS'], 'Nr of bits/datum (SEARCH mode data, else 1)')
    hdr['ZERO_OFF'] = ('*', 'Zero offset for SEARCH-mode data')
    hdr['SIGNINT'] = (0, '1 for signed ints in SEARCH-mode data, else 0')
    hdr['NSUBOFFS'] = ('*', 'Subint offset (Contiguous SEARCH-mode files)')
    hdr['NCHAN'] = (nchan, 'Number of channels/sub-bands in this file')
    hdr['CHAN_BW'] = (fits_hdul['SUBINT'].header['CHAN_BW'], '[MHz] Channel/sub-band width')
    hdr['REFFREQ'] = freq_ref
    hdr['DM'] = (dm, '[cm-3 pc] DM for post-detection dedisperion')
    hdr['RM'] = (0., '[rad m-2] RM for post-detection deFaraday')
    hdr['NCHNOFFS'] = ('*', 'Channel/sub-band offset for split files')
    nbin = data.shape[-1]
    hdr['NSBLK'] = (nbin, 'Samples/row (SEARCH mode, else 1)')
    hdr['NSTOT'] = ('*', 'Total number of samples (SEARCH mode, else 1)')
    hdr['EXTVER'] = (1, 'auto assigned by template parser')
    
    col_indexval = fits.Column(name='INDEXVAL', format='1D', array=[np.float64(0)])
    col_tsubint = fits.Column(name='TSUBINT', format='1D', array=[np.float64(tsubint)], unit='s')
    col_offs_sub = fits.Column(name='OFFS_SUB', format='1D', array=[np.float64(offs_sub)], unit='s')
    col_period = fits.Column(name='PERIOD', format='1D', array=[np.float64(tsubint)], unit='s')
    col_aux_dm = fits.Column(name='AUX_DM', format='1D', array=[np.float64(0)])
    col_aux_rm = fits.Column(name='AUX_RM', format='1D', array=[np.float64(0)])
    col_dat_freq = fits.Column(name='DAT_FREQ', format='%dD'%nchan, unit='MHz', array=[np.float64(dat_freq)])
    col_dat_wts = fits.Column(name='DAT_WTS', format='%dE'%nchan, array=[np.float32(dat_wts)])
    col_dat_offs = fits.Column(name='DAT_OFFS', format='%dE'%len(dat_offs), array=[np.float32(dat_offs)])
    col_dat_scl = fits.Column(name='DAT_SCL', format='%dE'%len(dat_scl), array=[np.float32(dat_scl)])
    col_data = fits.Column(name='DATA', format='%dI'%(data.shape[0]*data.shape[1]*data.shape[2]), unit='Jy', dim='(%d,%d,%d)'%(data.shape[-1], data.shape[-2], data.shape[-3]), array=[data.astype(np.int16)])
    hdu = fits.BinTableHDU.from_columns([col_indexval, col_tsubint, col_offs_sub, col_period, col_aux_dm, col_aux_rm, col_dat_freq, col_dat_wts, col_dat_offs, col_dat_scl, col_data], header=hdr, nrows=1)
    del col_data
    return(hdu, stt)


def primary(fits_hdul, stt):
    print('generate primary hdu')
    decimal, stt_imjd = np.modf(stt)
    stt_imjd = int(stt_imjd)
    stt_offs, stt_smjd = np.modf(decimal*86400)
    stt_smjd = int(stt_smjd)
    hdu = fits_hdul[0]
    hdu.header['STT_IMJD'] = stt_imjd
    hdu.header['STT_SMJD'] = stt_smjd
    hdu.header['STT_OFFS'] = stt_offs
    hdu.header['OBSFREQ'] = freq_center
    hdu.header['OBS_MODE'] = 'PSR'
    hdu.header['SRC_NAME'] = 'FRB20201124A'
    hdu.header['CAL_FREQ'] = '*'
    hdu.header['CAL_DCYC'] = '*'
    hdu.header['CAL_PHS'] = '*'
    hdu.header['CAL_NPHS'] = '*'
    return(hdu)


def shift(p0, nbin_shift):
    nbin = len(p0)
    p0_fft = np.fft.rfft(p0)
    angle = 2*np.pi*np.arange(nbin//2+1)*(nbin_shift/float(nbin))
    p1_fft = p0_fft*np.exp(1j*angle)
    p1 = np.fft.irfft(p1_fft)/float(nbin)
    return(p1)
    

def fits_to_ar(fitsname_list, arg):
    burst_mjd, burst_filename_index, burst_subint, burst_bin, dm = arg
    with fits.open(fitsname_list[burst_filename_index]) as hdul:
        nbin = hdul['SUBINT'].header['NSBLK']
        nsubint = hdul['SUBINT'].header['NAXIS2']
        tsubint = hdul['SUBINT'].data[0]['TSUBINT']
        freq = hdul['SUBINT'].data[0]['DAT_FREQ']
        t_delay = calD*dm/freq**2
        t_delay -= t_delay.min()
        print(t_delay.max())
        tbin = tsubint/float(nbin)
        print(tsubint, nbin, tbin)
        bin_delay = t_delay/tbin
        bin_delay_frac, bin_delay_int = np.modf(bin_delay)
        bin_delay_int = np.int_(bin_delay_int)
        print('bin_delay_int', bin_delay_int.max())
        delaymax_nsubint = int(np.ceil(t_delay.max()/tsubint))
        print('delaymax_nsubint', delaymax_nsubint)
        st_filename_index = burst_filename_index
        st_subint = burst_subint - nsubint_advance
        st_bin = burst_bin
        end_filename_index = burst_filename_index
        end_subint = burst_subint + delaymax_nsubint + nsubint_delay
        length_subint = nsubint_advance + nsubint_delay
        length_bin = length_subint*nbin
        print('length_bin', length_bin)
        end_bin = burst_bin
    while st_subint <= -1:
        if st_filename_index >= 1:
            st_filename_index -= 1
            with fits.open(fitsname_list[st_filename_index]) as hdul:
                nsubint_pre = hdul['SUBINT'].header['NAXIS2']
                st_subint += nsubint_pre
        else:
            st_subint = 0
            st_bin = 0
    while end_subint >= nsubint:
        if end_filename_index <= (len(fitsname_list) - 2):
            with fits.open(fitsname_list[end_filename_index]) as hdul:
                nsubint_next = hdul['SUBINT'].header['NAXIS2']
                end_subint -= nsubint_next
            end_filename_index += 1
        else:
            with fits.open(fitsname_list[end_filename_index]) as hdul:
                nsubint_next = hdul['SUBINT'].header['NAXIS2']
                nbin_next = hdul['SUBINT'].data['DATA'].shape[1]
                end_subint = nsubint_next
                end_bin = nbin_next
    print(st_filename_index, end_filename_index, st_subint, end_subint, st_bin, end_bin)
    data_list = []
    for filename_index in range(st_filename_index, end_filename_index+1):
        filename = fitsname_list[filename_index]
        with fits.open(filename) as hdul:
            print(filename)
            npol = hdul['SUBINT'].header['NPOL']
            nchan = hdul['SUBINT'].header['NCHAN']
            if filename_index == st_filename_index:
                data_list.extend(hdul['SUBINT'].data['DATA'][st_subint, st_bin:].astype(np.int16).squeeze(axis=-1).tolist())
                if filename_index == end_filename_index:
                    data_list.extend(hdul['SUBINT'].data['DATA'][st_subint+1:end_subint].astype(np.int16).squeeze(axis=-1).reshape(-1, npol, nchan).tolist())
                    data_list.extend(hdul['SUBINT'].data['DATA'][end_subint, :end_bin].astype(np.int16).squeeze(axis=-1).tolist())
                else:
                    data_list.extend(hdul['SUBINT'].data['DATA'][st_subint+1:].astype(np.int16).squeeze(axis=-1).reshape(-1, npol, nchan).tolist())
            elif filename_index == end_filename_index:
                data_list.extend(hdul['SUBINT'].data['DATA'][:end_subint].astype(np.int16).squeeze(axis=-1).reshape(-1, npol, nchan).tolist())
                data_list.extend(hdul['SUBINT'].data['DATA'][end_subint, :end_bin].astype(np.int16).squeeze(axis=-1).tolist())
            else:
                data_list.extend(hdul['SUBINT'].data['DATA'].astype(np.int16).squeeze(axis=-1).reshape(-1, npol, nchan).tolist())
    data_list = np.array(data_list).astype(np.int16)
    print('all', data_list.shape, data_list.dtype)
    data_all = []
    for pol in range(npol):
        data_pol = []
        for chan in range(nchan):
            #if length_bin+bin_delay_int[chan] >= data_list.shape[0]:
            #    print(length_bin+bin_delay_int[chan], data_list.shape[0])
            p = shift(data_list[bin_delay_int[chan]:length_bin+bin_delay_int[chan],pol,chan], bin_delay_frac[chan]).astype(np.float32)
            print('data_chan', p.shape)
            data_pol.append(p)
        data_pol = np.array(data_pol)
        print('data_pol', data_pol.shape)
        data_all.append(data_pol)
    del data_list
    data_all = np.array(data_all)
    print(data_all.shape, data_all.dtype)

    #with fits.open(fitsname_list[st_fitsname]) as hdul:

    with fits.open(fitsname_list[st_filename_index]) as fits_hdul:
        subint_hdu, stt = subint(fits_hdul, st_filename_index, st_subint, st_bin, end_filename_index, end_subint, end_bin, dm, data_all)
        nbin = data_all.shape[-1]
        del data_all
        primary_hdu = primary(fits_hdul, stt)
        history_hdu = history(fits_hdul, nbin=nbin, tbin=tbin, dm=dm)
        hdul = fits.HDUList([primary_hdu, history_hdu, subint_hdu])
        newfilename = fitsname_list[st_filename_index].rsplit('.', 1)[0] + '_%.10f.ddar'%burst_mjd
        if os.path.isfile(newfilename):
            os.remove(newfilename)
        hdul.writeto(newfilename)
        hdul.close()

def parse_arguments(argv):
    print("argv: ", argv)
    parser = argparse.ArgumentParser()
    parser.add_argument('--info', type=str, dest='infofile', help='info filename')
    parser.add_argument('fitsname_list', type=str, nargs='+', help='fits filename')
    args = parser.parse_args(argv)
    return(args)

def read_info(filename):
    # 读取filename(a.fits)对应的文件里的第1，2列数据（下标从0开始，有第0列），并且这两列数据保存为float类型（但是你给我的文件里的数据应该不太对）
    # 你可以尝试备份一个a.fits，然后文件内容只保留两行数字
    mjd_list, dm_list = np.loadtxt(filename, unpack=True, usecols=(1, 2), dtype=float)
    if not(type(mjd_list) == np.ndarray):
        mjd_list = np.array([mjd_list])
        dm_list = np.array([dm_list])
    # 打印这两列数据
    print(mjd_list, dm_list)
    return(mjd_list, dm_list)

if __name__ == '__main__':
    # 解析命令行参数包括[--info, a.fits, b.ar]
    # 添加类似--info之类的变量保存参数，e.g.，python slice.py --info a.fits b.ar
    args = parse_arguments(sys.argv[1:]) 
    # 根据前一步得到的infofile变量，变量的值是a.fits,读取对应的文件，这里就是读取a.fits
    burst_mjd_list, dm_list = read_info(args.infofile)
    # 这里burst_mjd_list和dm_list就是从read_info函数返回的结果
    # 然后是调用mjd_find函数，参数是第二个文件名（b.ar），和上面的burst_mjd_list、dm_list这两列数据
    # 现在报错在mjd_find函数，跳转到这个函数看
    arg_list = mjd_find(args.fitsname_list, burst_mjd_list, dm_list)
    func = partial(fits_to_ar, args.fitsname_list)
    for arg in arg_list:
        func(arg)
