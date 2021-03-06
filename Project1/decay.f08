program decay
  real :: pu(200), an(200), t(200)
  real, parameter :: tau = 126.58
  real :: tt = 5.0*tau
  real :: pu0 = 100.
  integer :: ns
  integer :: nt
  real :: dt
  open(7, file = "results")
  print*, "Enter the time step size:  "
  read*, ns
  nt = 200/ns
  dt = tt*ns/200.
  pu(1)=pu0
  t(1) = 0.0
100 format(3(2x, e12.5))
  do i=1, nt-1
     t(i+1) = t(i)+dt
     an(i+1) = 100*exp(-t(i+1)/tau)
     pu(i+1) = pu(i)*(1-dt/tau)
     write(7,100), t(i+1), an(i+1), pu(i+1)
  enddo
  close(7)
end program decay
  
  
