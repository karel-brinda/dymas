#
# PROGRAMS
#

rule prog_dwgsim:
    message:
        "Compiling DwgSim"
    output:
        DWGSIM
    shell:
        """
            cd src_ext
            cd dwgsim
            git submodule init
            git submodule update
            make
            cd ..
            cd ..
            cp src_ext/dwgsim/dwgsim {output[0]}
        """

rule prog_samtools:
    message:
        "Compiling SamTools"
    output:
        SAMTOOLS
    shell:
        """
            cd src_ext
            cd samtools
            make
            cd ..
            cd ..
            cp src_ext/samtools/samtools {output[0]}
        """

rule prog_htslib:
    message:
        "Compiling HtsLib"
    output:
        TABIX,
        BGZIP
    shell:
        """
            cd src_ext
            cd htslib
            make
            cd ..
            cd ..
            cp src_ext/htslib/tabix {output[0]}
            cp src_ext/htslib/bgzip {output[1]}
        """

rule prog_bcftools:
    message:
        "Compiling BcfTools"
    output:
        BCFTOOLS
    shell:
        """
            cd src_ext
            cd bcftools
            make
            cd ..
            cd ..
            cp src_ext/bcftools/bcftools {output[0]}
        """


# BWA

rule prog_bwa:
    message:
        "Compiling BWA "
    output:
        BWA
    run:
        shell("""
            cd src_ext
            cd bwa
            make
            cd ..
            cd ..
            cp src_ext/bwa/bwa {output[0]}
        """)

# CALL VARIANTS

rule prog_call_variants:
    message:
        "Compiling CallVariants "
    output:
        CALLVARIANTS
    run:
        shell("""
            cd call_variants
            cmake .
            make
            cd ..
            cp call_variants/call_variants {output[0]}
        """)



# LAVEnder
