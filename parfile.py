"""StagYY par file handling."""

from __future__ import annotations
from copy import deepcopy
import typing

import f90nml

from .config import CONFIG_DIR
from .error import NoParFileError

if typing.TYPE_CHECKING:
    from pathlib import Path
    from f90nml.namelist import Namelist

PAR_DFLT_FILE = CONFIG_DIR / 'par'
PAR_DEFAULT = f90nml.namelist.Namelist({
    'switches': {
        'verbose': False,
        'try_continue': False,
        'compressible': False,
        'dens_strat': True,
        'dens_actual': False,
        'melting': False,
        'composition': False,
        'phase_changes': False,
        'geoid_kernel_mode': False,
        'tracers': False,
        'cont_rafts': False,
        'cont_tracers': False,
        'clb_experiment': False,
        'chem_bm1': False,
        'pvk_bm': False,
        'Io_tidal_heating': False,
        'atmosphere': False,
        'multig_solve': True,
        'plates_analyse': False,
        'dimensional_units': False,
        'total_pressure': False,
        'dens_read_Fabio': False,
        'visc_read_Fabio': False,
        'quiet': False,
    },

    'geometry': {
        'shape': 'spherical',
        'nxtot': 1,
        'nytot': 512,
        'nztot': 64,
        'aspect_ratio': [1.0, 10.0, 1.0],
        'theta_position': 'default',
        'zspacing_mode': 'constant',
        'dresl_topbot': 1.0,
        'D_dimensional': 2890.e3,
        'D_dim_top': 0.0e3,
        'anti_squeeze': True,
        'anti_squeeze_r_fraction': 0.5,
        'dresl_air': 1.0,
        'dresl_surf': 1.0,
        'dresl_cmb': 1.0,
        'dresl_ppv': 1.0,
        'dresl_660': 1.0,
        'dresl_400': 1.0,
        'wresl_air': 0.1,
        'wresl_surf': 0.1,
        'wresl_cmb': 0.1,
        'wresl_ppv': 0.1,
        'wresl_660': 0.1,
        'wresl_400': 0.1,
        'r_cmb': 1.19,
        'yy_MinOverlap': True,
        'kmaxb': 0.25,
        'kmaxt': 0.25,
        'npbl': 10,
    },

    'refstate': {
        'Di0': 1.18,
        'ra0': 1.e5,
        'nradiogenic': 1,
        'Rh': [0.0],
        'Rh_tstart': 0.,
        'drho_thermal': 0.125,
        'perplex_properties': False,
        'perplex_hz_file': 'harzburgite.dat',
        'perplex_bs_file': 'basalt.dat',
        'perplex_pr_file': 'primordial.dat',
        'perplex_py_file': 'pyrolite.dat',
        'perplex_dT': 100.,
        'Tref_surf': 0.64,
        'rhoref_surf': [3240., 3080., 2900., 2900., 3080., 3080., 7000.],
        'gr_s': [1.3],
        'drho_surf': 1.0,
        'drho_cmb': 4337.,
        'q_gamma': [1.0],
        'delT0_expan': [6.0],
        'ex_tkappa': [3.0],
        'ak_expan': [1.4],
        'c_dependent_heating': False,
        'dHeat_dprim': 1.0,
        'dHeat_dbasalt': 1.0,
        'Rh_halflife': ['BIG'],
        'deltaT_dimensional': 2500.0,
        'g_dimensional': 9.81,
        'gravity_3D': False,
        'core_superheat': 0.0,
        'tcond_dimensional': 3.0,
        'core_tcond': 46.0,
        'dens_dimensional': 3300.,
        'expan_dimensional': 3.e-5,
        'Cp_dimensional': 1200.,
        'core_cooling': False,
        'core_model': 'simple',
        'core_Kppm': 0.0,
        'core_Tmelt0': 5600,
        'core_heatcap': 6.38e12,
        'phase_assemblage_varies_with_C': False,
        'air_density': 1.e-3,
        'topregion_adiabatic': False,
        'topregion_z': 1.0,
        'topregion_thalf': 'BIG',
        'Birch_Murnaghan': False,
        'K0': [210.e9],
        'Kp': [3.9],
        'heterogeneous_heating': False,
        'Hs_zbot': 0.,
        'Hs_ztop': 1.,
        'Hs_bot': 0.,
        'Hs_top': 0.,
        'Hs_mode': 1,
    },

    'boundaries': {
        'topT_mode': 'isothermal',
        'topT_val': 1.0,
        'botT_mode': 'iso',
        'botT_val': 0.0,
        'outT_val': -1.0,
        'topV_mode': 'free-slip',
        'botV_mode': 'free-slip',
        'x_patch': 0.5,
        'y_patch': 0.5,
        'r_patch': 0.1,
        'x_spread': 0.0,
        'v_spread': 0.0,
        'nx_plates': 2,
        'ny_plates': 2,
        'x_bc': 'ww',
        'y_bc': 'ww',
        'v_mantle': 0.0,
        'air_layer': False,
        'air_thickness': 0.1,
        'air_threshold': 0.8,
        'virtual_bndry_distance': -1.,
        'zero_surface_mean_flow': True,
        'Tsurf_eqm': 300.,
        'topT_locked_subsolar': 300.,
        'topT_locked_farside': 200.,
        'vbc_file_stem': 'vbc',
        'plateid_file_stem': 'pid',
        'vbc_file_interval_Myr': 1.0,
        'vbc_file_start_Myr': -70.,
        'platerecon_time_origin': 0.0,
        'platerecon_time_init': 0.0,
        'platerecon_time_end': 0.0,
        'BottomPhaseChange': False,
        'BotPphase': 1.,
        'TopPhaseChange': False,
        'TopPphase': 1.,
    },

    't_init': {
        'imode_t': 'cells',
        'amp_t': 0.00,
        'blthick': 0.1,
        't0_init': 0.5,
        'z0_t': 0.5,
        'w0_t': 0.5,
        'dip': 0.0,
        'length': 0.0,
        'ocean_age': 60.0,
        'cont_thick': 100.e3,
    },

    'timein': {
        'nsteps': 1,
        'nwrite': 1,
        'alpha_adv': 0.5,
        'alpha_diff': 1.0,
        'iord': 2,
        'advection_scheme': 'MPDATA',
        'stoptime': 'hhmm',
        'dt_write': 'BIG',
        'finish_at_time': 'BIG',
        'TVD_limiter': 2.,
        'diffusion_implicit': False,
        'diffusion_beta': 1.0,
        'diffusion_errmax': 1.e-4,
        'diffusion_maxits': 100,
        'diffusion_alpha': 0.6,
        'diffusion_nrelax': 3,
        'density_jump_stabilization': False,
        'density_jump_theta': 1.0,
        'density_jump_simplify': True,
        'PBSTimeRequested': 168.0,
    },

    'viscosity': {
        'ietalaw': 0,
        'E_eta': [0.0],
        'V_eta': [0.0],
        'Pdecay_V': ['BIG'],
        'Ts_eta': -1.0,
        'n_eta': 3.5,
        'eta0': 1.0,
        'T0_eta': 0.5,
        'd0_eta': 0.5,
        'stress0_eta': [1.0],
        'deta_p': [1.0],
        'deta_p_correct_jumps': False,
        'diffusion_creep': True,
        'dislocation_creep': False,
        'eta_max': 1.e5,
        'eta_min': 1.e-5,
        'eta_minmax_depthmax': 'BIG',
        'deta_basalt': 1.0,
        'deta_ccrust': 1.0,
        'deta_primordial': 1.0,
        'deta_metal': 1.0,
        'deta_water': 1.0,
        'etalaw_basalt': 1,
        'etalaw_ccrust': 1,
        'etalaw_metal': 1,
        'etalaw_melt': 1,
        'etalaw_primordial': 1,
        'etalaw_water': 1,
        'c0eta_basalt': 0.0,
        'c0eta_ccrust': 0.0,
        'c0eta_primordial': 0.0,
        'c0eta_metal': 0.0,
        'c0eta_water': 0.0,
        'weak_line': False,
        'weak_dx': 0.1,
        'weak_dz': 0.05,
        'weak_eta': 1.0,
        'strong_cont_rafts': False,
        'strong_eta': 1.0,
        'strong_dz': 0.05,
        'vertonly_eta': False,
        'horzonly_eta': False,
        'plasticity': False,
        'c_dependent_yieldpars': False,
        'stressY_eta': 'BIG',
        'dstressY_eta_dp': 0.0,
        'cohesion_eta': 'BIG',
        'frictionCoeff_eta': 'BIG',
        'stressY_basalt': 'BIG',
        'dstressY_basalt': 0.0,
        'cohesion_basalt': 'BIG',
        'frictionCoeff_basalt': 'BIG',
        'stressY_ccrust': 'BIG',
        'dstressY_ccrust': 0.0,
        'cohesion_ccrust': 'BIG',
        'frictionCoeff_ccrust': 'BIG',
        'stressY_metal': 'BIG',
        'dstressY_metal': 0.0,
        'cohesion_metal': 'BIG',
        'frictionCoeff_metal': 'BIG',
        'stressY_primordial': 'BIG',
        'dstressY_primordial': 0.0,
        'cohesion_primordial': 'BIG',
        'frictionCoeff_primordial': 'BIG',
        'dstressY_eta_water': 1.0,
        'water_dependent_stressY_eta': False,
        'd_etalaw': 1,
        'Rheal_law': 'constant',
        'E_Rh': 0.0,
        'F_eta': 0.0,
        'eta_melt': False,
        'deta_melt': 1.0,
        'mean_T_eta': False,
        'T0_Tmean': 0.5,
        'E_eta_Tmean': 0.0,
        'eta_conv': 0.01,
        'alpha_eta': 1.0,
        'maxits_eta': 20,
        'bmoore_eta': False,
        'aniso_ep': False,
        'visc_interp_law': 'g',
        'phase_dep_Eeta': False,
        'eta_air': 1.,
        'PressureDepRheology': False,
        'PressureDepVact': False,
        'RaFromRheolPref': False,
    },

    'grainsize': {
        'graingrowth_k': 1.,
        'graingrowth_p': 4.,
        'graingrowth_E': 300.e3,
        'grainreduction_C': 1.,
        'grainsize0_eta': 1.,
        'grainsize_n_eta': 3.0,
        'GS_ForcedPiezometric': True,
        'GS_TwoPhases': False,
        'GS_PiezometerModel': 'homogeneous',
        'GG_k0': [2.49813e7, 2.49813e7],
        'GG_p': [2.0, 2.0],
        'GG_E': [2.e5, 2.e5],
        'GS_InitSize': [1e2, 1e2],
        'GS_gamma': [1e6, 1e6],
        'curv_k0': 74943.9,
        'curv_E': 2.e5,
        'curv_q': 1.5,
        'curv_gamma': 1.e6,
        'curv_Init': 1e2,
        'GSD_sigma': 0.8,
        'GS_fG0': 1.e-2,
        'GS_fI0': 0.0,
        'transition_depth_GS': [410.e3, 500.e3, 660.e3, 2740.e3],
        'GSAfterPhaseTrans': 5.e0,
        'curvDownThrough660': 5.e0,
    },

    'iteration': {
        'maxits': 50,
        'minits': 1,
        'errmax': 1.e-3,
        'alpha_mom': 0.7,
        'alpha_cont': 0.9,
        'redblack': False,
        'extra_lid_relax': False,
        'nlid_relax': 1,
        'tlid': 0.2,
        'extra_hiresid_relax': False,
        'nhi_relax': 1,
        'normalize_res_by_eta': False,
        'relax_kernel': 'classic',
    },

    'multi': {
        'maxcoarseits': 200,
        'nrelax1': 3,
        'nrelax2': 3,
        'nhmin': 4,
        'nzmin': 4,
        'nzpnmin': 1,
        'alpha_multi': 1.0,
        'matrix_dep_pinterp': True,
        'matrix_dep_vinterp': False,
        'ncpus_per_node': 8,
        'nppcpu_opt_samenode': 64,
        'nppcpu_opt_xnode': 1024,
        'more_coarse_its': True,
        'f_cycle': False,
        'direct_coarse_soln': False,
        'idle_duplicates': True,
    },

    'ioin': {
        'input_file': 'null',
        'input_frame': 1,
        'output_file_stem': 'test',
        't_write': True,
        'vp_write': False,
        'eta_write': False,
        'c_write': False,
        'bs_write': False,
        'hz_write': False,
        'air_write': False,
        'cc_write': False,
        'primordial_write': False,
        'f_write': False,
        't_spectrum_write': False,
        'vm_write': False,
        'stress_write': False,
        'g_write': False,
        'tra_write': False,
        'metal_write': False,
        'vd_write': False,
        'edot_write': False,
        'age_write': False,
        'nmelt_write': False,
        'rho_write': False,
        'grainsize_write': False,
        'hpe_write': False,
        'water_write': False,
        'K_Ar_write': False,
        'oxides_write': False,
        'ph_write': False,
        'residue_write': False,
        'nrho_write': False,
        'w_write': False,
        'delete_old_trafiles': True,
        'delete_old_nonhdf_files': False,
        'torpol_write': False,
        'svel_write': False,
        'pvel_write': False,
        'bvel_write': False,
        'topo_write': False,
        'lyap_write': False,
        'divvor_write': False,
        'crust_write': False,
        'heatflux_write': False,
        'heatflux_spectrum_write': False,
        'lmax': 16,
        'stress_axis_write': False,
        'trapercell_write': False,
        'write_32bit_precision': False,
        'MORBprof_write': False,
        'save_file_framestep': 10,
        'overwrite_old_files': False,
        'restart_from_meshed_fields_only': False,
        'hdf5_output_folder': '+hdf5',
        'hdf5_input_folder': '+hdf5',
        'MaxFileSizeAllowed': 100000000,
        'MaxFileSizeAllowedTra': 100000000,
    },

    'compin': {
        'imode_comp': 'layered',
        'zcomp': 0.5,
        'amp_comp': 0.0,
        'ra_comp': [0.0],
        'lenardic_filter': False,
        'outC_val': -1.0,
        'dzcomp': 0.1,
    },

    'melt': {
        'imode_melt': 'whatever',
        'ra_melt': 0.0,
        'mr_melt': 1.e6,
        'Tsol0': 0.5,
        'dTsol_dz': 1.0,
        'latent_heat': 1.0,
        'amp_melt': 0.02,
        'eruption': False,
        'erupt_fraction': 1.0,
        'intrusion': False,
        'intrude_fraction': 1.0,
        'tzintrusion': False,
        'tzintrude_fraction': 1.0,
        'outF_val': -1.0,
        'erupt_mode': 'all',
        'solidus_function': 'simple',
        'd_intrude': 0.0,
        'intrude_position': 'surface',
        'harzburgite_melts': False,
        'metal_melts': True,
        'suppress_asth': False,
        'c_dependent_solidus': False,
        'd_erupt_Earth': 1.0,
        'erupt_threshold': 0.0,
        'deltaTsol_depletion_dimensional': 60.,
        'deltaTsol_water_dimensional': 0.,
        'ddens_sol_liq_dimensional': 500.,
        'eta_liquid_dimensional': 10.,
        'k0_dimensional': 3.e-10,
        'p_dependent_solidus': False,
        'Cf_dependent_Tmelting': False,
        'melt_phase_systems': False,
        'melt_segregation': False,
        'erupt_T_lith': 1400.,
        'magma_effective_tcond': False,
        'magma_tcond_factor': 1.e5,
        'magma_topTBL_const': 1.e-7,
        'fractional_xtallisation_n_melting': False,
        'trackTTGsource': False,
    },

    'phase': {
        'nphase_systems': 1,
        'Ol_frac_ref': 0.6,
        'basalt_frac_ref': 0.2,
        'effective_Cp_alpha': True,
        'scale_PCdepths': False,
        'g0_dimensional_PCdepths': 9.81,
        'D0_dimensional_PCdepths': 2890.e3,
        'sys_ol': 1,
        'sys_pxgt': 2,
        'sys_melt_ol': 3,
        'sys_melt_pxgt': 4,
        'sys_prim': 5,
        'sys_ccrust': 6,
        'sys_metal': 7,
    },

    'continents': {
        'ncont': 1,
        'cont_radius': [0.1],
        'cont_startpos': [0.5],
        'cont_offsetplot': True,
        'rafts_move': False,
        'cont_collideaction': 'ignore',
        'cont_Biot': 1.e6,
        'cont_thickness': 100.e3,
    },

    'tracersin': {
        'ntracers': 50,
        'ntracers_per_cell': -1,
        'imode_tra': 'even+ran',
        'B_basalt': 0.0,
        'B_ccrust': 0.0,
        'B_metal': 0.0,
        'd_crust': 0.1,
        'w_crust': 0.0,
        'Ctr_truncate': False,
        'k_fe': 0.85,
        'Fe_eut': 0.8,
        'Fe_cont': 0.1,
        'Ctr_lininterp': True,
        'Ttr_lininterp': True,
        'H2Otr_lininterp': True,
        'trastrain_diagnostics': False,
        'tracers_everywhere': True,
        'tracers_strain': False,
        'tracers_timemelt': False,
        'tracers_recstartpos': False,
        'tracers_advord': 2,
        'tracers_interp2ord': True,
        'tracers_weakcrust': False,
        'weakcrust_maxdepth': 0.3,
        'tracers_temperature': False,
        'oxides_compositions': False,
        'basalt_harzburgite': False,
        'continental_crust': False,
        'tracers_weakfault': False,
        'traceelement_hpe': False,
        'traceelement_water': False,
        'traceelement_K_Ar': False,
        'track_GrainSize': False,
        'metal': False,
        'ddens_SiO2': 0.0,
        'ddens_MgO': 0.0,
        'ddens_FeO': 0.0,
        'ddens_XO': 0.0,
        'dTmelting_dFeO': 0.0,
        'primordial_layer': True,
        'd_primordial': 0.1,
        'B_primordial': 0.0,
        'imode_primordial': 'layer',
        'imode_metal': 'top_layer',
        'd_metal': 0.0,
        'tracers_horizontaladvection': False,
        'tracers_noadvection': False,
        'Dpartition_FeO': 1.0,
        'Dpartition_hpe': 1.0,
        'Dpartition_water': 1.0,
        'Dpartition_K': 1.0,
        'Dpartition_Ar': 1.0,
        'outgas_fraction_water': 1.0,
        'outgas_fraction_Ar': 1.0,
        'ingas_water': False,
        'ingas_depth': 10.e3,
        'IntrudedBasaltHydrationFraction': 0.0,
        'overturn': False,
        'mode_init_overturn': 'linear',
        'Zdiff_h2o': 0.1,
        'diff_h2o': 0.5,
        'water_at_top': True,
        'topH2O_val': 0.0,
        'cH2O_mantle': 1.0,
        'diffusion_water': False,
    },

    'plot': {
        'plot_file_stem': 'image',
        'npix': 200000,
        'dots': True,
        'auto_t_scale': True,
        'z_xyslice': 0.5,
        't_superadiabatic': False,
        't_plot': True,
        'v_plot': False,
        'p_plot': False,
        'eta_plot': False,
        'rho_plot': False,
        'c_plot': False,
        'f_plot': False,
        'pd_plot': False,
        'dT_plot': False,
        'vm_plot': False,
        'stress_plot': False,
        'edot_plot': False,
        'g_plot': False,
        'tra_plot': False,
        'vd_plot': False,
        'air_plot': False,
        'oxides_plot': False,
        'hpe_plot': False,
        'water_plot': False,
        'K_Ar_plot': False,
        'primordial_plot': False,
        'rhs_plot': False,
        'bs_plot': False,
        'hz_plot': False,
        'cc_plot': False,
        'tcond_plot': False,
        'Cp_plot': False,
        'expan_plot': False,
        'grainsize_plot': False,
        'age_plot': False,
        'nmelt_plot': False,
        'strain_plot': False,
        'ph_plot': False,
        'lyap_plot': False,
        'residue_plot': False,
        'trapercell_plot': False,
        'imgtype': 'png',
    },

    'postprocessing': {
    },

    'atm_stuff': {
        'atm_model': 'simple',
    },

    'magma_oceans_in': {
        'magma_oceans_mode': False,
        'evolving_magma_oceans': False,
    },

})


def _enrich_with_par(par_nml: Namelist, par_file: Path) -> None:
    """Enrich a par namelist with the content of a file."""
    par_new = f90nml.read(str(par_file))
    for section, content in par_new.items():
        if section not in par_nml:
            par_nml[section] = {}
        for par, value in content.items():
            try:
                content[par] = value.strip()
            except AttributeError:
                pass
        par_nml[section].update(content)


def readpar(par_file: Path, root: Path) -> Namelist:
    """Read StagYY par file.

    The namelist is populated in chronological order with:

    - :data:`PAR_DEFAULT`, an internal dictionary defining defaults;
    - :data:`PAR_DFLT_FILE`, the global configuration par file;
    - ``par_name_defaultparameters`` if it is defined in ``par_file``;
    - ``par_file`` itself;
    - ``parameters.dat`` if it can be found in the StagYY output directories.

    Args:
        par_file: path of par file.
        root: path on which other paths are rooted. This is usually par.parent.
    Returns:
        A :class:`f90nml.namelist.Namelist`. It is a case-insensitive dict of
        dict of values with first key being the namelist and second key the
        names of variables.
    """
    par_nml = deepcopy(PAR_DEFAULT)

    if PAR_DFLT_FILE.is_file():
        _enrich_with_par(par_nml, PAR_DFLT_FILE)
    else:
        PAR_DFLT_FILE.parent.mkdir(exist_ok=True)
        f90nml.write(par_nml, str(PAR_DFLT_FILE))

    if not par_file.is_file():
        raise NoParFileError(par_file)

    par_main = f90nml.read(str(par_file))
    if 'default_parameters_parfile' in par_main:
        par_dflt = par_main['default_parameters_parfile'].get(
            'par_name_defaultparameters', 'par_defaults')
        par_dflt = root / par_dflt
        if not par_dflt.is_file():
            raise NoParFileError(par_dflt)
        _enrich_with_par(par_nml, par_dflt)

    _enrich_with_par(par_nml, par_file)

    par_out = root / par_nml['ioin']['output_file_stem'] / '_parameters.dat'
    if par_out.is_file():
        _enrich_with_par(par_nml, par_out)
    par_out = root / par_nml['ioin']['hdf5_output_folder'] / 'parameters.dat'
    if par_out.is_file():
        _enrich_with_par(par_nml, par_out)
    return par_nml
